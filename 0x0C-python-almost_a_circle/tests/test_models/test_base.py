#!/usr/bin/python3
""" Test's for base class """

from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """ Test's for base class methods """

    def test___init__(self):
        """ Test's for init method """

        self.assertTrue(Base.__init__.__doc__)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base("2").id, "2")
        self.assertEqual(Base().id, 2)
