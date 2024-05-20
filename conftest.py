import pytest
from src.applications.ui.github_ui import GithubUI
from src.applications.api.githhub_api import GitHubAPIClient
from selenium import webdriver

from src.application.ui.github_ui import GithubUI



@pytest.fixture
def github_ui_app():
    driver = webdriver.Chrome()

    # Presteps:
      # 1. Navigate to Github app
    github_ui_app = GithubUI(browser= driver)
    github_ui_app.open_browser()

    # Generator 
    yield github_ui_app

    # Poststeps:
    github_ui_app.close_browser()

    @pytest.fixture
    def git_hub_api_client():
        githubui_app = GitHubAPIClient()

        yield github_ui_app