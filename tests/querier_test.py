import json
import os
import os.path as path
import unittest

from src import Authenticator, Querier


class TestQuerier(unittest.TestCase):
    def setUp(self):
        PUBLIC_KEY = '1234'
        PRIVATE_KEY = 'abcd'
        TIME_STAMP = '1'
        self.auth = Authenticator(PUBLIC_KEY, PRIVATE_KEY, TIME_STAMP)

        test_path = path.abspath(path.curdir)+'/tests/'
        test_data_file = test_path+'test_data/public_docs.json'
        self.public_documentation = json.load(open(test_data_file))

    def test_get_querier_string(self):
        pass

    def test_parameter_verification(self):
        q = Querier('characters', self.auth)
        q.load_values(self.public_documentation)
        possible_values = q.get_possible_lists()
        self.assertEqual(possible_values['name']['type'], str)
        self.assertEqual(possible_values['nameStartsWith']['type'], str)
        self.assertEqual(possible_values['orderBy']['type'], str)
        self.assertEqual(possible_values['orderBy']['input-type'], list)
        self.assertEqual(possible_values['orderBy']['possible_values'],
                         ['name', 'modified', '-name', '-modified'])

    def test_querier_add_parameter_attribute_error(self):

        q = Querier('comics', self.auth)
        q.load_values(self.public_documentation)
        list_of_possible_parameters_and_their_types = q.get_possible_lists()\
            .keys()

        # Check that attribute error is raised if incorrect search parameter is
        # given
        with self.assertRaises(AttributeError) as error:
            q.add_parameters(name=3)
        error_msg = str(error.exception)
        expected_error_msg = \
            'Attribute {!r} not valid for entity {!r}' +\
            ' try one of the following {!r}.'
        msg = expected_error_msg.format(
            'name',
            'comics',
            list_of_possible_parameters_and_their_types
        )
        self.assertEqual(error_msg, msg)

    def test_querier_add_parameter_given_search_value_type_error(self):
        # Check that
        q = Querier('comics', self.auth)
        q.load_values(self.public_documentation)
        # list_of_possible_parameters_and_their_types = q.get_possible_lists()

        with self.assertRaises(TypeError) as error:
            q.add_parameters(title=3)
        error_msg = str(error.exception)
        expected_error_msg = \
            '{!r} given for parameter {!r} is invalid type should be {!r}.'\
            .format(
                type(3),
                'title',
                str
            )
        self.assertEqual(error_msg, expected_error_msg)

        with self.assertRaises(TypeError) as error:
            q.add_parameters(series=3020)
        with self.assertRaises(TypeError) as error:
            q.add_parameters(series=['3020'])
        with self.assertRaises(ValueError) as error:
            q.add_parameters(limit=200)
        with self.assertRaises(TypeError) as error:
            q.add_parameters(orderBy=[200])
        with self.assertRaises(ValueError) as error:
            q.add_parameters(orderBy=['value'])
        # print(error.exception)


if __name__ == "__main__":
    unittest.main()
