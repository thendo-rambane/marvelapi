import json
import os
import os.path as path
# import requests
from typing import overload

from .authenticator import Authenticator as Auth
from .entity import Entity
from .querier import Querier

PUBLIC_KEY = '9b6d7545e698ec76a8673df57089edbc'
PRIVATE_KEY = 'd55e975ae3c3a0e3041d7f8688e126c3f0d517dc'

# auth = Auth(PUBLIC_KEY, PRIVATE_KEY)

class Error(Exception):
    pass

q_test_path = path.abspath(path.curdir)+'/tests/'
q_test_data_file = q_test_path+'test_data/public_docs.json'
public_documentation = json.load(open(q_test_data_file))


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
        else:
            return None

    def character_by_id(self, id: int):
        self.__get_by_id('characters', id)

    def characters(self, **kwargs):
        self.__get('characters', **kwargs)

    def creator_by_id(self, id: int):
        self.__get_by_id('creators', id)

    def creators(self, **kwargs):
        self.__get('creators', **kwargs)

    def comic_by_id(self, id: int):
        self.__get_by_id('comics', id)

    def comics(self, **kwargs):
        self.__get('comics', **kwargs)

    def event_by_id(self, id: int):
        self.__get_by_id('events', id)

    def events(self, **kwargs):
        self.__get('events', **kwargs)

    def series_by_id(self, id: int):
        self.__get_by_id('series', id)

    def series(self, **kwargs):
        self.__get('series', **kwargs)

    def story_by_id(self, id: int):
        self.__get_by_id('stories', id)

    def stories(self, **kwargs):
        self.__get('stories', **kwargs)


# if __name__ == "__main__":
#     m = MarvelAPI(PUBLIC_KEY, PRIVATE_KEY)
#     m.characters(name='james', nameStartsWith='ll')
