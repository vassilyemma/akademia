from src.application.ui.base_app import BaseApp
from src.application.ui.pages.login_page import LoginPage
from selenium import webdriver

class GithubUI(BaseApp):

   # Initialize the constants
  URL = "https://github.com/login"

  def __init__(self, browser) -> None:
    super().__init__(browser)
  
    # initial login page for github app
    self.login_page = LoginPage(browser, '//*[@id="login_field"]', '//*[@id="password"]', '//*[@id="login"]/div[4]/form/div/input[13]','//*[@id="js-flash-container"]/div/div/div')

  def try_login(self, username: str, password: str):
    return self.login_page.try_login(username, password)

  def open_browser(self):
    self.navigate_to(self.URL)
  
  def close(self):
    self.close_browser()
  