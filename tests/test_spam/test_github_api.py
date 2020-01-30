from unittest.mock import Mock

import pytest

from spam import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/11460643?v=4'
    resp_mock.json.return_value = {
        "login": "Ernanidacosta", "id": 11460643,
        "avatar_url": url,
    }
    get_mock = mocker.patch('spam.github_api.requests.get')
    #   get_original = github_api.requests.get
    get_mock.return_value=resp_mock
    return url

    #    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('ernanidacosta')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('ernanidacosta')
    assert 'https://avatars3.githubusercontent.com/u/11460643?v=4' == url
