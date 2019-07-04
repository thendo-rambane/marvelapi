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

test_path = path.abspath(path.curdir)+'/tests/'
test_data_files = os.listdir(path=test_path+'test_data/')
test_json = {}
for test_file in test_data_files:
    if test_file.find('marvel') > -1:
        key = test_file.split('.')[0].split('-')[1]
        test_json[key] = json.load(open(test_path+'/test_data/'+test_file))
results = test_json['character']['data']['results']

q_test_path = path.abspath(path.curdir)+'/tests/'
q_test_data_file = q_test_path+'test_data/public_docs.json'
public_documentation = json.load(open(q_test_data_file))


class MarvelAPI():
    """docstring for MA"""

    def __init__(self, public_key: str, private_key: str):
        self.auth = Auth(public_key, private_key)
        self.querier = None

    def __run_endpoint_request(self, query: str):
        # request = requests.get(query)
        # if req.status_code != 200:
        # 	print('ERROR')
        # response = request.json()
        # return response['data']['results']
        return []

    def __get_by_id(self, entity: str, id: int):
        self.querier = Querier(entity, self.auth)
        query = self.querier.get_query_string(id)
        result = self.__run_endpoint_request(query)
        return Entity(entity, result)

    def __get(self, entity: str, **kwargs) -> list:
        """Key word argument overload"""
        self.querier = Querier(entity, self.auth)
        self.querier.load_values(public_documentation)
        self.querier.add_parameters(**kwargs)
        query = self.querier.get_query_string()
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
