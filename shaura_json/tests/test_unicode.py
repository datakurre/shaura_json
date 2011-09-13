# -*- coding: utf-8 -*-
"""Integration tests"""

import unittest2 as unittest
from corejet.core import Scenario, story, scenario, given, when, then

from shaura_json import testing


@story(id="17891603", title=(u"As developer I want to store "
                             u"<unicode> into <str> fields"))
class As_developer_I_want_to_store_unicode_into_str_fields(unittest.TestCase):

    layer = testing.PyramidLayer

    @scenario("Store <unicode> to 'zope.schema.Id'-field")
    class Store_unicode_to_zopeschemaIIdfield(Scenario):

        @given("I've got a <unicode> string of an id")
        def Ive_got_an_unicode_string_of_an_id(self):
            self.json_value = u"Unicode String"
            self.assertIsInstance(self.json_value, unicode)
            self.assertFalse(isinstance(self.json_value, str))

        @when("I adapt it to IFieldValue for a 'zope.schema.Id'-field")
        def I_adapt_it_to_IFieldValue_for_a_zopeschemaIIdfield(self):
            import zope.schema
            from shaura_json.interfaces import IFieldValue
            self.field_value = self.layer.config.registry.getMultiAdapter(
                (zope.schema.Id(), self.json_value), IFieldValue)

        @then("I get a <str> representation of that string")
        def I_get_a_str_representation_of_that_string(self):
            self.assertEquals(self.json_value, self.field_value)
            self.assertIsInstance(self.field_value, str)
            self.assertFalse(isinstance(self.field_value, unicode))

    @scenario("Store <unicode> to 'zope.schema.ASCIILine'-field")
    class Store_unicode_to_zopeschemaIASCIILinefield(Scenario):

        @given("I've got a <unicode> string of a string")
        def Ive_got_an_unicode_string_of_a_string(self):
            self.json_value = u"Unicode String"
            self.assertIsInstance(self.json_value, unicode)
            self.assertFalse(isinstance(self.json_value, str))

        @when("I adapt it to IFieldValue for a 'zope.schema.ASCIILine'-field")
        def I_adapt_it_to_IFieldValue_for_a_zopeschemaIASCIILinefield(self):
            import zope.schema
            from shaura_json.interfaces import IFieldValue
            self.field_value = self.layer.config.registry.getMultiAdapter(
                (zope.schema.ASCIILine(), self.json_value), IFieldValue)

        @then("I get a <str> representation of that string")
        def I_get_a_str_representation_of_that_string(self):
            self.assertEquals(self.json_value, self.field_value)
            self.assertIsInstance(self.field_value, str)
            self.assertFalse(isinstance(self.field_value, unicode))

    @scenario("Store <unicode> to 'zope.schema.URI'-field")
    class Store_unicode_to_zopeschemaIURIfield(Scenario):

        @given("I've got a <unicode> string of an URI")
        def Ive_got_an_unicode_string_of_an_URI(self):
            self.json_value = u"http://www.google.com/"
            self.assertIsInstance(self.json_value, unicode)
            self.assertFalse(isinstance(self.json_value, str))

        @when("I adapt it to IFieldValue for a 'zope.schema.URI'-field")
        def I_adapt_it_to_IFieldValue_for_a_zopeschemaIURIfield(self):
            import zope.schema
            from shaura_json.interfaces import IFieldValue
            self.field_value = self.layer.config.registry.getMultiAdapter(
                (zope.schema.URI(), self.json_value), IFieldValue)

        @then("I get a <str> representation of that string")
        def I_get_a_str_representation_of_that_string(self):
            self.assertEquals(self.json_value, self.field_value)
            self.assertIsInstance(self.field_value, str)
            self.assertFalse(isinstance(self.field_value, unicode))
