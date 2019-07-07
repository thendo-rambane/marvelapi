"""Querier.

This module implements the Querier class whose objects will allow users to
make requests to the Marvel APIs REST services.

The Querier class has two methods:
    __build_query_string - Private abstract method used to build endpoint URIs
    get_query_string - returns the built endpoint URI

"""
from abc import ABC, abstractmethod
import json
import requests
from datetime import date
# import requests

from .authenticator import Authenticator as Auth


class Querier():
    """Class represents a Querier object.

    parameters:
        authenticator - an authenticator object to help build the URIs.

    """

    def __init__(self, entity: str, authenticator: Auth):
        """Constructor.

        Initialise authenticator.

        parameters:
            entity - a string that describes which entity the endpoint
                is searching
            authenticator - an authenticator object to help build the URI.

        """
        self.parameters = {}
        self.entity = entity

        self.__authenticator = authenticator
        self.__query_string = ''
        self.__possible_values = {}

    def __check_type(self, parameter, value, type_expected, msg=None):
        """Verify that value is of expected type"""

        if not isinstance(value, type_expected):
            type_error_msg = '{!r} given for parameter {!r}' +\
                ' is invalid type should be {!r}.'
            msg = type_error_msg.format(
                type(value),
                parameter,
                type_expected)
            raise TypeError(msg)

    def __check_list_paramaters(self, parameter_name,
                                current_parameter, value):
        """
        Verify that given value for a list type search parameter
        meets specification
        """

        # Check that given value is a list if not raise type error
        if isinstance(value, list):
            # Check that all values in given list are of the correct type
            for parameter in value:
                if not isinstance(parameter, current_parameter['type']):
                    type_error_msg = \
                        'In value list for parameter{!r},' +\
                        ' {!r} is of type {!r}, {!r} expected.'
                    msg = type_error_msg.format(
                        parameter_name,
                        parameter,
                        type(parameter),
                        current_parameter['type'])

                    raise TypeError(msg)
        else:

            type_error_msg = \
                'Value {!r} given for parameter {!r} is of type {!r}, {!r}' +\
                ' expected.'
            msg = type_error_msg.format(
                value,
                parameter_name,
                type(value),
                list)
            raise TypeError(msg)

    def __check_parameter(self, parameter_name: str, value):
        """Verify that given search parameter meets specification"""
        self.__load_possible_entity_values()

        possible_values = self.get_possible_lists()
        # Check if given parameter name is an accepted search parameter if not
        # raise Attribute error
        if parameter_name in possible_values.keys():
            current_parameter = possible_values[parameter_name]

            # Check if search parameter requires a list as a parameter.
            if current_parameter['input-type']:
                # Check that lists holds values of correct type
                self.__check_list_paramaters(
                    parameter_name, current_parameter, value)

            # Check if search parameter accepts only certain values.
            # Verify that given values are accepted
            if 'possible_values' in current_parameter.keys():
                if isinstance(current_parameter['possible_values'], list):
                    for possible_value in value:
                        if possible_value not in \
                                current_parameter['possible_values']:
                            value_error_msg = \
                                '{!r} given for parameter {!r},' +\
                                ' expected value should be in {!r}.'
                            msg = value_error_msg.format(
                                possible_value,
                                parameter_name,
                                current_parameter['possible_values'])
                            raise ValueError(msg)
                else:
                    start = current_parameter['possible_values'][0]
                    end = current_parameter['possible_values'][1] + 1
                    if value not in range(start, end):
                        value_error_msg = \
                            '{!r} given for parameter {!r},' +\
                            ' value between {!r} expected.'
                        msg = value_error_msg.format(
                            value,
                            parameter_name,
                            current_parameter['possible_values'])
                        raise ValueError(msg)

            else:
                # Verify that all given values are of the correct type
                self.__check_type(parameter_name, value,
                                  current_parameter['type'])
        else:
            attr_error_msg = \
                'Attribute {!r} not valid for entity {!r}' +\
                ' try one of the following {!r}.'
            msg = attr_error_msg.format(
                parameter_name,
                self.entity,
                possible_values.keys())
            raise(AttributeError(msg))

    def __build_query_string(self, item_id=None):
        """Create a query string from the given parameter.

        If item_id is passed in only an id query is built

        parameters:
            search_params - a dictionary of search parameters
            item_id - if this parameter is given an id based endpoint is
                generated.
        """
        if item_id:
            self.__query_string = '/' + str(item_id) + '?'
        else:
            edited = False
            query_string = ''
            for key, value in self.parameters.items():
                if isinstance(value, list):
                    if edited:
                        query_string += '&'
                    query_string += str(key) + '=' + \
                        ','.join([item for item in value])
                    edited = True
                elif key in ['limit', 'offset']:
                    if edited:
                        query_string += '&'
                    query_string += str(key) + '=' + str(value)
                    edited = True
                else:
                    if edited:
                        query_string += '&'
                    query_string += str(key) + '=' + value
                    edited = True
            if edited:
                query_string += '&'

            self.__query_string = '?' + query_string

    def __load_possible_entity_values(self, test_values=None):
        if not test_values:
            res = requests.get('http://gateway.marvel.com/docs/public')
            if res.status_code != 200:
                print(res.status_code)
            test_values = res.json()
        entity_values = {}
        TYPES = {'int': int,
                 'Date': str,
                 'string': str,
                 'boolean': bool
                 }
        for api in test_values['apis']:
            if str(api['path']).find('Id') == -1:
                entity_name = str(api['path']).split('/')[-1]
                entity_values[entity_name] = {}
                parameters = api['operations'][0]['parameters']

                for parameter in parameters:
                    parameter_name = parameter['name']
                    entity_values[entity_name][parameter_name] = {}
                    entity_values[entity_name][parameter_name]['type'] = \
                        TYPES[parameter['dataType']]

                    if parameter['allowMultiple']:
                        entity_values[entity_name][parameter_name][
                            'input-type'] = list
                    else:
                        entity_values[entity_name][parameter_name][
                            'input-type'] = None

                    if 'allowableValues' in parameter.keys():
                        if parameter['allowableValues']['valueType'] == 'LIST':
                            entity_values[entity_name][parameter_name][
                                'possible_values'] = \
                                parameter['allowableValues']['values']
                        elif parameter['allowableValues']['valueType']\
                                == 'RANGE':
                            entity_values[entity_name][parameter_name][
                                'possible_values'] = \
                                (parameter['allowableValues']['min'],
                                 parameter['allowableValues']['max'])

        self.__possible_values = entity_values

    def load_values(self, values=None):
        self.__load_possible_entity_values(values)

    def add_parameters(self, **kwarg):
        """Add search parameter using key word arguments"""
        if not len(kwarg):
            possible_values = self.get_possible_lists()
            attr_error_msg = \
                'No search parameters given' +\
                ' try one of the following {!r}.'
            msg = attr_error_msg.format(possible_values.keys())
            raise(AttributeError(msg))
        else:
            for key, value in kwarg.items():
                self.__add_parameter(key, value)

    def __add_parameter(self, parameter_name: str, value):
        """Add search parameters and values"""

        self.__check_parameter(parameter_name, value)
        # If search parameter exists and its value is of type list then only
        # unique values are included in search
        if (parameter_name in self.parameters.keys()) and \
                (isinstance(self.parameters[parameter_name], list)):
            for parameter in value:
                if parameter not in self.parameters[parameter_name]:
                    self.parameters[parameter_name].append(value)
        # Add values to a given parameter or create a parameter if it does
        # not exist
        else:
            self.parameters[parameter_name] = value

    def get_possible_lists(self):
        self.__load_possible_entity_values()
        return self.__possible_values[self.entity]

    def get_query_string(self, item_id=None) -> str:
        """Return the query string.

        parameters:
            search_params - a dictionary of search parameters
            item_id - if this parameter is given an id based endpoint is
                generated.

        return:
            A URI type string that is used to run RESTful queries

        """
        self.__build_query_string(item_id)

        return 'https://gateway.marvel.com/v1/public/' + self.entity +\
            self.__query_string + self.__authenticator.get_auth_string()
