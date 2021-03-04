import unittest

from zope.component import queryMultiAdapter
from zope.publisher.browser import TestRequest

from zope.fanstatic.testing import ZopeFanstaticBrowserLayer

import mycave.tests
from mycave.app import Mycave

# In this file we create a unittest, a functional unittest.

def test_pytest():
    '''
    Testing the py.test test runner in Grok.
    '''
    assert True is False


class MyTestCase(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1, 1)

browser_layer = ZopeFanstaticBrowserLayer(mycave.tests)

class MyFunctionalTestCase(unittest.TestCase):

    layer = browser_layer

    def test_foo(self):
        index = queryMultiAdapter((Mycave(), TestRequest()), name='index')
        self.assertNotEqual(index, None)

        # There is no view called 'index2'
        index2 = queryMultiAdapter((Mycave(), TestRequest()), name='index2')
        self.assertEqual(index2, None)

