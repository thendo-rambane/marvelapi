import json
import os
import os.path as path
import requests
from typing import overload

from .authenticator import Authenticator as Auth
from .entity import Entity
from .querier import Querier


class Error(Exception):
    pass


class MarvelAPI():
    """docstring for MA"""

    def __init__(self, public_key: str, private_key: str):
        self.__auth = Auth(public_key, private_key)
        self.__querier = None

    def __run_endpoint_request(self, query: str):
        request = requests.get(query)
        if request.status_code != 200:
            error = request.json()['status']
            raise Error(error)
        response = request.json()
        return response['data']['results']

    def __get_by_id(self, entity: str, id: int):
        self.__querier = Querier(entity, self.__auth)
        query = self.__querier.get_query_string(id)
        result = self.__run_endpoint_request(query)
        return Entity(entity, result[0])

    def __get(self, entity: str, **kwargs) -> list:
        """Key word argument overload"""
        self.__querier = Querier(entity, self.__auth)
        self.__querier.add_parameters(**kwargs)
        query = self.__querier.get_query_string()
        results = self.__run_endpoint_request(query)
        if results:
            return [Entity(entity, result) for result in results]

    def character_by_id(self, id: int):
        return self.__get_by_id('characters', id)

    def get_characters_where(self, **kwargs):
        return self.__get('characters', **kwargs)

    def creator_by_id(self, id: int):
        return self.__get_by_id('creators', id)

    def get_creator_where(self, **kwargs):
        return self.__get('creators', **kwargs)

    def comic_by_id(self, id: int):
        return self.__get_by_id('comics', id)

    def get_comic_where(self, **kwargs):
        return self.__get('comics', **kwargs)

    def event_by_id(self, id: int):
        return self.__get_by_id('events', id)

    def get_event_where(self, **kwargs):
        return self.__get('events', **kwargs)

    def series_by_id(self, id: int):
        return self.__get_by_id('series', id)

    def get_series_where(self, **kwargs):
        return self.__get('series', **kwargs)

    def story_by_id(self, id: int):
        return self.__get_by_id('stories', id)

    def get_stories_where(self, **kwargs):
        return self.__get('stories', **kwargs)
