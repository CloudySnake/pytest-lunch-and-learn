import unittest
from unittest import mock

from src.simple_adder.adder import add_up, BadData, add_up_with_api


class TestSimpleAdder(unittest.TestCase):
    def test_add_up(self):
        res = add_up(1, 1)
        self.assertEqual(res, 2)

    def test_string_throws_exception(self):
        self.assertRaises(BadData, add_up, "1", 2)

    @mock.patch("src.simple_adder.adder.requests")
    @mock.patch("src.simple_adder.adder.totally_cool_api_call")
    def test_mocked_api_call(self, mock_api, mock_requests):
        mock_api.return_value = {"url": "http://pytest/rules/ok", "content": 100}
        mock_requests.return_value = "BOOM"

        assert add_up_with_api("any_url", 100) == 200
