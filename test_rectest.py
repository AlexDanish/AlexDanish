# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRectest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_rectest(self):
    self.driver.get("https://guru.qahacking.ru/index.php/about")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.ID, "hobbies-checkbox-1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-9:nth-child(6) #hobbies-checkbox-1").click()
    self.driver.find_element(By.ID, "submit").click()
  
