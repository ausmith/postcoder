#!/usr/bin/env python3

import mock
import pytest

from postcoder.__main__ import is_postcode_valid, get_postcode_info, get_nearest_postcodes_list

MOCKED_FUNC_NAME = 'postcoder.__main__._make_postcodes_io_request'

class TestPostcoder(object):
    def test_invalid_postcode(self, validate_invalid_response):
        with mock.patch(MOCKED_FUNC_NAME, return_value=validate_invalid_response) as validate_mock:
            assert is_postcode_valid("someval") == False


    def test_valid_postcode(self, validate_valid_response):
        with mock.patch(MOCKED_FUNC_NAME, return_value=validate_valid_response) as validate_mock:
            assert is_postcode_valid("CB3 0FA") == True


    def test_info_result(self, info_response):
        with mock.patch(MOCKED_FUNC_NAME, return_value=info_response) as info_mock:
            assert get_postcode_info("CB3 0FA") == {
                    "postcode": "CB3 0FA",
                    "country": "England",
                    "region": "East of England",
                }


    def test_info_result_with_bad_input(self):
        with mock.patch(MOCKED_FUNC_NAME, return_value={"result": {}}) as info_mock:
            assert get_postcode_info("someval") == {
                    "postcode": "",
                    "country": "Unknown",
                    "region": "Unknown",
                }


    def test_nearest_result(self, nearest_response):
        with mock.patch(MOCKED_FUNC_NAME, return_value=nearest_response) as nearest_mock:
            assert get_nearest_postcodes_list("CB3 0FA") == [
                    {"postcode": "CB3 0FA", "country": "England", "region": "East of England"},
                    {"postcode": "CB3 0GT", "country": "England", "region": "East of England"},
                ]
