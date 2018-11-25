#!/usr/bin/env python

import pytest

#from postcoder.__main__ import # import the things we want

class TestPostcoder(object):
    def test_example_test(self, example_fixture):
        assert example_fixture == {}
