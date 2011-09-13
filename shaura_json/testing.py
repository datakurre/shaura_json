# -*- coding: utf-8 -*-
"""zope.testrunner layers"""

from pyramid import testing


class PyramidLayer(object):

    @classmethod
    def setUp(cls):
        cls.config = testing.setUp()

        import pyramid_zcml
        cls.config.include(pyramid_zcml)
        cls.config.load_zcml("shaura_json:configure.zcml")

    @classmethod
    def tearDown(cls):
        testing.tearDown()

    @classmethod
    def testSetUp(cls):
        pass

    @classmethod
    def testTearDown(cls):
        pass
