"""Querier.

This module implements the Querier class whose objects will allow users to
make requests to the Marvel APIs REST services.

The Querier class has two methods:
    __build_query_string - Private abstract method used to build endpoint URIs
    get_query_string - returns the built endpoint URI

"""
from abc import ABC, abstractmethod
from .authenticator import Authenticator as Auth


class Querier(ABC):
    """Class represents a Querier object.

    parameters:
        authenticator - an authenticator object to help build the URIs.

    """

    def __init__(self, collection: str, authenticator: Auth):
        """Constructor.

        Initialise authenticator.

        parameters:
            collection - a string that describes which collection the endpoint
                is searching
            authenticator - an authenticator object to help build the URI.

        """
        self.__authenticator = authenticator
        self.__collection = collection
        self.__query_string = ''

    @abstractmethod
    def __build_query_string(self, search_params: dict, item_id=None):
        """Create a query string from the given parameter.

        parameters:
            search_params - a dictionary of search parameters
            item_id - if this parameter is given an id based endpoint is
                generated.

        """
        if (item_id != None):
            self.__query_string = self.__collection + '/' + str(item_id)+'/'

    def get_query_string(self, search_params: dict, item_id=None) -> str:
        """Return the query string.

        parameters:
            search_params - a dictionary of search parameters
            item_id - if this parameter is given an id based endpoint is
                generated.

        return:
            A URI type string that is used to run RESTful queries

        """
        self.__build_query_string(search_params, item_id)
        return 'https://gateway.marvel.com/v1/public/' + self.__query_string \
            + self.__authenticator.get_auth_string()
