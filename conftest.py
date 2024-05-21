import pytest
from selenium import webdriver
from src.applications.ui.github_ui import GithubUI
from src.applications.api.githhub_api import GitHubAPIClient
from selenium import webdriver

from src.application.ui.github_ui import GithubUI



@pytest.fixture
class GithubUI:
    def __init__(self, browser):
        self.browser = browser

    def open_browser(self):
        self.browser.get("https://github.com")

    def close_browser(self):
        self.browser.quit()

class GitHubAPIClient:
    # Placeholder for GitHubAPIClient implementation
    pass

@pytest.fixture
def github_ui_app():
    driver = webdriver.Chrome()
    github_ui_app = GithubUI(browser=driver)
    
    # Presteps: Navigate to Github app
    github_ui_app.open_browser()

    # Yield control back to the test
    yield github_ui_app

    # Poststeps: Close the browser
    github_ui_app.close_browser()

@pytest.fixture
def github_api_client():
    github_api_client = GitHubAPIClient()

    # Yield control back to the test
    yield github_api_client

# Example usage in a test
def test_github_ui(github_ui_app):
    # Your test code here
    pass

def test_github_api(github_api_client):
    # Your test code here
    pass