# -*- coding: utf-8 -*-
import unittest
import unittest.mock

from test_project import common


class TestSanity(unittest.TestCase):
    def test_sanity(self) -> None:
        common.test1()
