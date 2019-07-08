import json
import os
import os.path as path
import unittest

from marvelapi import Authenticator, Querier


class TestQuerier(unittest.TestCase):
    def setUp(self):
        PUBLIC_KEY = '1234'
        PRIVATE_KEY = 'abcd'
        TIME_STAMP = '1'
        self.auth = Authenticator(PUBLIC_KEY, PRIVATE_KEY, TIME_STAMP)

        test_path = path.abspath(path.curdir)+'/marvelapi/tests/'
        test_data_file = test_path+'test_data/public_docs.json'
        self.public_documentation = json.load(open(test_data_file))

    def test_get_querier_string(self):
        q = Querier('characters', self.auth)
        query_string = q.get_query_string(1011334)
        expected_string = 'https://gateway.marvel.com/v1/public/characters/' +\
            '1011334?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150'
        self.assertEqual(query_string, expected_string)

    def test_parameter_verification(self):
        q = Querier('characters', self.auth)
        possible_values = q.get_possible_lists()
        self.assertEqual(possible_values['name']['type'], str)
        self.assertEqual(possible_values['nameStartsWith']['type'], str)
        self.assertEqual(possible_values['orderBy']['type'], str)
        self.assertEqual(possible_values['orderBy']['input-type'], list)
        self.assertEqual(possible_values['orderBy']['possible_values'],
                         ['name', 'modified', '-name', '-modified'])

    def test_querier_add_parameter_attribute_error(self):

        q = Querier('comics', self.auth)
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
        q = Querier('comics', self.auth)

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
        error_msg = str(error.exception)
        msg = 'Value {!r} given for parameter {!r} is of type {!r}, {!r}' +\
            ' expected.'
        expected_error_msg = msg.format(
            3020,
            'series',
            type(3020),
            list
        )
        self.assertEqual(error_msg, expected_error_msg)

        with self.assertRaises(TypeError) as error:
            q.add_parameters(series=['3020', 1520])
        error_msg = str(error.exception)
        msg = 'In value list for parameter{!r},' +\
            ' {!r} is of type {!r}, {!r} expected.'
        expected_error_msg = msg.format(
            'series',
            '3020',
            type('3020'),
            int
        )
        self.assertEqual(error_msg, expected_error_msg)

        with self.assertRaises(ValueError) as error:
            q.add_parameters(limit=200)
        error_msg = str(error.exception)
        msg = '{!r} given for parameter {!r},' +\
            ' value between {!r} expected.'
        expected_error_msg = msg.format(
            200,
            'limit',
            (1, 100)
        )
        self.assertEqual(error_msg, expected_error_msg)

        with self.assertRaises(ValueError) as error:
            q.add_parameters(orderBy=['value'])
        error_msg = str(error.exception)
        msg = '{!r} given for parameter {!r},' +\
            ' expected value should be in {!r}.'
        expected_error_msg = msg.format(
            'value',
            'orderBy',
            [
                'focDate',
                'onsaleDate',
                'title',
                'issueNumber',
                'modified',
                '-focDate',
                '-onsaleDate',
                '-title',
                '-issueNumber',
                '-modified'
            ]
        )
        self.assertEqual(error_msg, expected_error_msg)


if __name__ == '__main__':
    unittest.main()
