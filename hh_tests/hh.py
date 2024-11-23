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
      driver.maximize_window()
      yield driver
      driver.close()
        
   @allure.feature('check remote job checklist in vacancies search')
   @allure.story('vacancies search') 
   @pytest.mark.tags("crirical_path", "login")   
   def test_checklist_remote_work(self, browser: webdriver.Firefox):
      with allure.step(f"Given: I've go to vacancies search {BASE_URL} url"):
         browser.get(BASE_URL+"/search/vacancy")
      with allure.step("I've found remote job selector"):
         remote_job_selector=browser.find_element(By.XPATH, "//input[@type='checkbox' and @name='schedule' and value='remote']").find_element(By.XPATH, "./../../..");
      with allure.step("I click on it"):
         remote_job_selector.click()
      with allure.step("I am on a search vacancies page by, the url contains remote jobs query"):
         url = selenium.getLocation()
         assert url.index('schedule=remote')!=-1         
         
   @allure.feature('check login pathway')      
   @pytest.mark.tags("crirical_path", "login")   
   @allure.story('login') 
   @pytest.mark.parametrize("name, password", [(os.getenv("USERNAME"), os.getenv("PASSWORD"))] )
   def test_success_login_by_password(self, browser: webdriver.Firefox , name, password):
      with allure.step("Given I am login page:"):
         browser.get(BASE_URL+'/login')
      with allure.step("I click on enter by password:"):
         browser.find_element(By.XPATH, "//a[@data-qa='expand-login-by-password']").click()
      with allure.step("I wait until password field"):
         password_field = WebDriverWait(browser, 10).until(
         EC.visibility_of(
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@data-qa='login-input-password']")))
            )
         )
      with allure.step("I enter login data"):
         name_field = browser.find_element(By.XPATH, "//input[data-qa='login-input-password']")
         print(name)
         name_field.send_keys(name)
         password_field.send_keys(password)
         browser.find_element(By.XPATH, "//button[data-qa='account-login-submit']").click()
      with allure.step("And it cookies contains crypted id"):
         assert browser.get_cookie('crypted_id')