#test hh.ru
from asyncio import sleep
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
   @allure.title("firefox driver")
   def browser(self):
      options = Options()
      driver=webdriver.Firefox(options=options)
      driver.maximize_window()
      yield driver
      driver.close()
   
   @allure.title("Test Search by remote job param")     
   @allure.epic("Web interface")
   @allure.feature('check remote job checklist in vacancies search')
   @allure.description("This is the demo test for unitcase woth  vacancies search. TBD: make search POD")
   @allure.story('vacancies search') 
   @allure.tag("crirical_path", "login")  
   @allure.severity(allure.severity_level.NORMAL)
   @allure.link("https://hh.ru/search/vacancy", name="HH search")
   @allure.issue("UI-123")
   @allure.testcase("TMS-123") 
   def test_checklist_remote_work(self, browser: webdriver.Firefox):
      with allure.step(f"Given: I've go to vacancies search {BASE_URL} url"):
         browser.get(BASE_URL+"/search/vacancy")
      with allure.step("I've found remote job selector"):
         sleep(2)
         remote_job_selector = WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox' and @name='schedule' and @value='remote'])[1]")));
      with allure.step("I click on it"):
         browser.execute_script("arguments[0].click();", remote_job_selector)
         remote_job_selector.click()
      with allure.step("I am on a search vacancies page by, the url contains remote jobs query"):
         url = selenium.getLocation()
         assert url.index('schedule=remote')!=-1         
        
         
   @allure.feature('check login pathway')      
   @allure.tag("crirical_path", "login")   
   @allure.story('login') 
   @allure.severity(allure.severity_level.CRITICAL)
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