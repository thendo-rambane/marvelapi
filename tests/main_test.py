import unittest
import json
import os
import unittest
import os.path as path

from src import MarvelAPI
from src import Entity

PUBLIC_KEY = '9b6d7545e698ec76a8673df57089edbc'
PRIVATE_KEY = 'd55e975ae3c3a0e3041d7f8688e126c3f0d517dc'


class TestAPI(unittest.TestCase):
    def setUp(self):
        test_path = path.abspath(path.curdir)+'/tests/'
        test_data_files = os.listdir(path=test_path+'test_data/')
        self.test_json = {}
        for test_file in test_data_files:
            if test_file.find('marvel') > -1:
                key = test_file.split('.')[0].split('-')[1]
                self.test_json[key] = json.load(
                    open(test_path+'/test_data/'+test_file))
        self.characters = self.test_json['character']['data']['results']

    def test_get_entity_by_id(self):
        M = MarvelAPI(PUBLIC_KEY, PRIVATE_KEY)
        test_entity = M.character_by_id(1011334)
        expected_entity = None
        for character in self.characters:
            if character['id'] == 1011334:
                expected_entity = Entity('characters', character)
                break
        self.assertEqual(test_entity, expected_entity)

    def test_get_entity_where(self):
        M = MarvelAPI(PUBLIC_KEY, PRIVATE_KEY)
        test_entity = M.get_characters_where(name='3-D Man')
        expected_entity = None
        for character in self.characters:
            if character['name'] == '3-D Man':
                expected_entity = Entity('characters', character)
                break
        self.assertEqual(test_entity, expected_entity)


if __name__ == "__main__":
    unittest.main()
