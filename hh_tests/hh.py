#test hh.ru
import datetime
from asyncio import sleep
from datetime import date
from functools import partialmethod
import os
from urllib.parse import urljoin
import allure
import pytest
from _pytest.monkeypatch import MonkeyPatch
from pytest_playwright.pytest_playwright import browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'https://hh.ru'
from inspect import getfullargspec
from selenium.webdriver.remote.webdriver import WebDriver

#PO implementation
class BasePage():
    def __init__(self, browser: WebDriver):
        self.browser=browser

    def get_element_by_qa(self, qa: str, wait:int=None):
        if wait is None:
            return self.browser.find_element(By.XPATH, f"//*[{qa}]")
        else:
            return WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.XPATH, f"//*[{qa}]")))


class LoginPage:
    def __init__(self, browser: WebDriver):
        self.browser=browser
        self.base_page=BasePage(browser)


    def login(self, username: str, password: str):
        self.base_page.get_element_by_qa("expand-login-by-password").click()
        pas_field= WebDriverWait(self.browser, 10).until(
                EC.visibility_of(self.base_page.get_element_by_qa("login-input-password", 10)))
        user_field=self.base_page.get_element_by_qa("account-signup-email")
        user_field.send_keys(username)
        pas_field.send_keys(password)
        self.base_page.get_element_by_qa("account-login-submit")


class VacancySearchPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.base_page = BasePage(browser)

    def search_by_remote_work(self):
        remote_job_selector = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='checkbox' and @name='schedule' and @value='remote'])[1]")));
        self.browser.execute_script("arguments[0].click();", remote_job_selector)


def sreenshot_on_fail(browser_attr='browser'):
    def decorator(cls):
        def with_screen_shot(self, fn, *args, **kwargs):
            try:
                return fn(self, *args, **kwargs)
            except Exception:
                browser = getattr(args, browser_attr)
                filename = 'screenshot-%s.png' % fn.__name__
                browser.get_screenshot_as_file(filename)
                raise

        for attr, fn in cls.__dict__.items():
            if attr.startswith('test_') and callable(fn) and browser_attr in getfullargspec(fn).args:
                setattr(cls, attr, partialmethod(with_screen_shot, fn))

        return cls

    return decorator


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


class TestBase():
    @pytest.fixture(scope="module", params=['Firefox', 'Chrome'], ids=["firefox", "chrome"])
    @allure.title("web driver")
    def browser(self, request: pytest.FixtureRequest):
        driver = None
        match request.param:
            case 'Firefox':
                options = FirefoxOption()
                options.add_argument('--headless')
                driver = webdriver.Firefox(options=options)
            case 'Chrome':
                options = ChromeOption()
                options.add_argument('--headless')
                driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.close()


    @pytest.fixture(scope="module")
    @allure.title("login page")
    def login_page(self, browser: WebDriver):
        yield LoginPage(browser)

    @pytest.fixture(scope="module")
    @allure.title("search page")
    def vacancy_search_page(self, browser: WebDriver):
        yield VacancySearchPage(browser)


    @pytest.fixture(scope="function", autouse=True)
    def pytest_browser_rel_path(self, browser, monkeypatch: MonkeyPatch):
        browser_get = browser.get

        def get_rel_url(rel_path: str):
            browser_get(urljoin(BASE_URL, rel_path))

        monkeypatch.setattr(browser, "get", get_rel_url)


    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)


    @pytest.fixture(scope="function", autouse=True)
    @allure.title("screenshot saver")
    def screenshot_saver_on_failure(self, request: pytest.FixtureRequest, browser: WebDriver,
                                    pytestconfig: pytest.Config):
        (yield)
        if request.node.rep_call.failed:
            screenshot_filename=f'{pytestconfig.getoption("image_path", "./")}hh-{date.strftime(datetime.datetime.now(), "%m-%d-%Y-%H-%M-%S")}-{request.function.__name__}.png'
            browser.save_screenshot(screenshot_filename)
            allure.attach.file("screenshot", screenshot_filename)


    @allure.title("Test Search by remote job param")
    @allure.epic("Web interface")
    @allure.feature("Check remote job checklist in vacancies search")
    @allure.description("This is the demo test for unit case for vacancies search")
    @allure.story("Vacancies search")
    @allure.tag("critical_path", "login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://hh.ru/search/vacancy", name="HH search")
    @allure.issue("UI-123")
    @allure.testcase("TMS-123")
    def test_checklist_remote_work(self, browser: WebDriver, vacancy_search_page:VacancySearchPage ):
        with allure.step(f"Given: I've go to vacancies search {urljoin(BASE_URL, 'search/vacancy')} url"):
            browser.get("search/vacancy")
        with allure.step("I search vacancies page by remote job checkbox"):
            vacancy_search_page.search_by_remote_work()
        with allure.step("I am on a search vacancies page by, the url contains remote jobs query"):
            sleep(2)
            WebDriverWait(browser, 10).until(EC.url_contains("schedule=remote"));


    @allure.feature("Check login pathway")
    @allure.tag("critical_path", "login")
    @allure.story("login")
    @allure.description("This is the demo test for linux")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://hh.ru/login", name="HH login")
    @pytest.mark.parametrize("username, password", [(os.getenv("USERNAME"), os.getenv("PASSWORD")),
                                                pytest.param("incorrect_name", "incorrect_password",
                                                             marks=pytest.mark.xfail(reason="incorrect username"))])
    def test_success_login_by_password(self, browser: WebDriver, username: str, password: str, login_page: LoginPage):
        with allure.step("Given I am login page:"):
            browser.get('/login')
        with allure.step(f"I login to hh as user {username} with password {password}"):
            login_page.login(username, password)
        with allure.step("And it cookies contains crypted id"):
            assert browser.get_cookie('crypted_id')
