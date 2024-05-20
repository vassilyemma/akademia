from src.application.ui.base_app import BaseApp

class LoginPage(BaseApp):
  
  # login methods
  def __init__(self, browser, login_fld: str, password_fld: str, login_btn: str, error_message_text: str):
    # super
    super().__init__(browser)

    # Initialize the constants
    self.USERNAME_FLD = login_fld
    self.PASSWORD_FLD = password_fld
    self.LOGIN_BTN = login_btn
    self.ERROR_MESSAGE = error_message_text
  
  def try_login(self, username: str, password: str):
    self.enter_input(self.USERNAME_FLD, username)
    self.enter_input(self.PASSWORD_FLD, password)
    self.click_btn(self.LOGIN_BTN)

  def check_wrong_creds_message(self):
    # Find error
    # Check the message with specific text "...."
    error_message = self.get_text(self.ERROR_MESSAGE)
    return "Incorrect username or password." in error_message
  
  def check_documentation_link(self):
    pass
    

  