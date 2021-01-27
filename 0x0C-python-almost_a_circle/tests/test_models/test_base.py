#!/usr/bin/python3
""" Test's for base class """

from unittest import TestCase
from models.base import Base
from models import base


class TestBase(TestCase):
    """ Test's for base class methods """

    def test___init__(self):
        """ Test's for init method """

        self.assertTrue(Base.__init__.__doc__)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base("2").id, "2")
        self.assertEqual(Base().id, 2)

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)
