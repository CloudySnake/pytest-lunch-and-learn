import pytest

from src.simple_adder.adder import add_up, BadData, add_up_with_api


def test_add_up():
    res = add_up(1, 1)
    assert res == 2


def test_string_throws_exception():
    with pytest.raises(BadData):
        add_up("1", 2)


def test_mocked_api_call(mocker):
    mock_api = mocker.patch("src.simple_adder.adder.totally_cool_api_call")
    mock_api.return_value = {"url": "http://pytest/rules/ok", "content": 100}

    mock_requests = mocker.patch("src.simple_adder.adder.requests")
    mock_requests.return_value = "BOO"

    assert add_up_with_api("any_url", 100) == 200
