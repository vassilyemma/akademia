def test_check_search_repo(git_hub_api_client):
    """
    1.send API request to find the repi named BLA
    2.Analyse the repsonse

    Expected result:
    number of repos == SMnumber
    """

    # 1. send API request to find the repi named BLA

    repos_number, response = it_hub_api_client.search_repos("BLA")

    # 2. Analyse the response
    response.raise_for_status()

    assert len(repos_number) == 10