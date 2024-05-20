def test_github_login(github_ui_app):
    """
    Summary: Negative Test for Login 
    steps:
        1. Navigate to login page
        2. Enter wrong creds
        3. Click login/signin button

    Expected result:
        Error saying "Incorrect username or password." appeared
    """

    # Enter wrong credential 
    github_ui_app.try_login(username = 'your_username', password = 'your_password')

    # Expected result
    assert github_ui_app.login_page.check_wrong_creds_message()