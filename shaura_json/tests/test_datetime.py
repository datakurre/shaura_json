# -*- coding: utf-8 -*-
"""Integration tests"""

import unittest2 as unittest
from corejet.core import Scenario, story, scenario, given, when, then

from shaura_json import testing


@story(id="17816957", title=(u"As developer I want to store "
                             u"RFC3339 timestamp on datetime field"))
class I_want_to_store_RFC_timestamp_on_datetime_field(unittest.TestCase):

    layer = testing.PyramidLayer

    @scenario("Convert RFC3339 timestamp to Python datetime")
    class Convert_RFC_timestamp_to_Python_datetime(Scenario):

        @given("I've got an RFC3339 unicode string "
               "of a specific date and time")
        def Ive_got_an_RFC_unicode_string_of_a_specific_date_and_time(self):
            self.json_value = u"1985-04-12T23:20:50.52Z"

        @when("I adapt it to IFieldValue for a zope.schema.Datetime field")
        def I_adapt_it_to_IFieldValue_for_a_zopeschemaDatetime_field(self):
            import zope.schema
            from shaura_json.interfaces import IFieldValue
            self.field_value = self.layer.config.registry.getMultiAdapter(
                (zope.schema.Datetime(), self.json_value), IFieldValue)

        @then("I get correct datetime representation of that date and time")
        def I_get_correct_datetime_representation_of_that_date_and_time(self):
            import datetime
            self.assertIsInstance(self.field_value, datetime.datetime)
            self.assertEquals(tuple(self.field_value.timetuple()),
                              (1985, 4, 12, 23, 20, 50, 4, 102, -1))

    @scenario("Convert RFC3339 timestamp without "
              "milliseconds to Python datetime")
    class Convert_RFC_timestamp_without_millis_to_Python_datetime(Scenario):

        @given("I've got an RFC3339 unicode string "
               "of a specific date and time without milliseconds")
        def Ive_got_an_RFC_unicode_string_of_a_specific_date_and_time(self):
            self.json_value = u"1985-04-12T23:20:50Z"

        @when("I adapt it to IFieldValue for a zope.schema.Datetime field")
        def I_adapt_it_to_IFieldValue_for_a_zopeschemaDatetime_field(self):
            import zope.schema
            from shaura_json.interfaces import IFieldValue
            self.field_value = self.layer.config.registry.getMultiAdapter(
                (zope.schema.Datetime(), self.json_value), IFieldValue)

        @then("I get correct datetime representation of that date and time")
        def I_get_correct_datetime_representation_of_that_date_and_time(self):
            import datetime
            self.assertIsInstance(self.field_value, datetime.datetime)
            self.assertEquals(tuple(self.field_value.timetuple()),
                              (1985, 4, 12, 23, 20, 50, 4, 102, -1))

    @scenario("Convert Python datetime to RFC3339 timestamp")
    class Convert_Python_datetime_to_RFC_timestamp(Scenario):

        @given("I got a certain date and time in a zope.schema.Datetime field")
        def I_got_a_certain_date_and_time_in_a_zopeschemaDatetime_field(self):
            from datetime import datetime

            value = datetime(1985, 4, 12, 23, 20, 50, 520000)

            import zope.interface
            import zope.schema

            class ExampleSchema(zope.interface.Interface):
                datetime = zope.schema.Datetime()

            class Example(object):
                zope.interface.implements(ExampleSchema)

            self.obj = Example()
            bound = ExampleSchema["datetime"].bind(self.obj)
            bound.set(self.obj, value)

        @when("I adapt that field and value for IJSONValue")
        def I_adapt_that_field_and_value_for_IJSONValue(self):
            from shaura_json import utils as json
            self.json_values = json.values(self.obj)

        @then("I get a RFC3339 unicode string representation of that value")
        def I_get_a_RFC_unicode_string_representation_of_that_value(self):
            self.assertIn("datetime", self.json_values)
            self.assertEquals(self.json_values["datetime"],
                              u"1985-04-12T23:20:50.52Z")

    @scenario("Convert Python datetime without milliseconds "
              "to RFC3339 timestamp")
    class Convert_Python_datetime_without_millis_to_RFC_timestamp(Scenario):

        @given("I got a certain date and time without milliseconds "
               "in a zope.schema.Datetime field")
        def I_got_a_certain_date_and_time_in_a_zopeschemaDatetime_field(self):
            from datetime import datetime

            value = datetime(1985, 4, 12, 23, 20, 50, 0)

            import zope.interface
            import zope.schema

            class ExampleSchema(zope.interface.Interface):
                datetime = zope.schema.Datetime()

            class Example(object):
                zope.interface.implements(ExampleSchema)

            self.obj = Example()
            bound = ExampleSchema["datetime"].bind(self.obj)
            bound.set(self.obj, value)

        @when("I adapt that field and value for IJSONValue")
        def I_adapt_that_field_and_value_for_IJSONValue(self):
            from shaura_json import utils as json
            self.json_values = json.values(self.obj)

        @then("I get a RFC3339 unicode string representation of that value")
        def I_get_a_RFC_unicode_string_representation_of_that_value(self):
            self.assertIn("datetime", self.json_values)
            self.assertEquals(self.json_values["datetime"],
                              u"1985-04-12T23:20:50Z")
