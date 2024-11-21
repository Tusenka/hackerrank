#test hh.ru
import os
import allure
import pip
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL='https://hh.ru'


class TestBase():
   @pytest.fixture
   def browser(self):
      options = Options()
      options.add_argument('--headless')
      driver=webdriver.Firefox(options=options)
      yield driver
      driver.close()
        
   
   @pytest.mark.tags("crirical_path", "login")   
   def test_checklist_remote_work(self, browser):
      browser.get(BASE_URL+'/search/vacancy')
      with allure.step(f"Given: I've go to vacancies search {BASE_URL} url"):
         browser.get(BASE_URL)
      with allure.step("I've found remote job selector"):
         remote_job_selector=browser.find_element(By.cssSelector("input[type='checkbox'][name='login']"));
         assert remote_job_selector is not None
      with allure.step("I click on it"):
         remote_job_selector.click()
      with allure.step("I am on a search vacancies page by, the url contains remote jobs query"):
         url = selenium.getLocation()
         assert url.index('schedule=remote')!=-1         
         
         
   @pytest.mark.tags("smoke", "login")
   @pytest.mark.parametrize("name, password", [(os.getenv("username"), os.getenv("password"))] )
   def test_success_login_by_password(self, browser, name, password):
      with allure.step("Given I am login page:"):
         browser.get(BASE_URL+'/login')
      with allure.step("I click on enter by password:"):
         browser.find_element(By.cssSelector("a[data-qa='expand-login-by-password']")).click()
      with allure.step("I wait until password field"):
         password_field = WebDriverWait(browser, 10).until(
         EC.presence_of_element_located(By.cssSelector("input[data-qa='login-input-password]")))
      with allure.step("I enter login data"):
         name_field = browser.find_element(By.cssSelector("input[data-qa='login-input-password]"))
         name_field.send_key(name)
         password_field.send_keys(password)
         browser.find_element(By.cssSelector("button[data-qa='account-login-submit']"))
      with allure.step("And it cookies contains crypted id"):
         assert browser.getCookieNamed('crypted_id')