from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BaseApp:
  def __init__(self, browser ) -> None:
    self.browser = browser

  def navigate_to(self, url):
    self.browser.get(url)

  def enter_input(self, locator: str, text: str):
    input = WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, locator)))
    input.clear()
    input.send_keys(text)

  def click_btn(self, locator: str):
    sign_in_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
    sign_in_button.click()
  
  def get_text(self, locator: str):
    error_message_element = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
    return error_message_element.text
  
  def close_browser(self):
    self.browser.close()