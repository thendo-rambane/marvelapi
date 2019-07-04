"""Unit Test module for marvel api interface"""
from datetime import datetime
import json
import os
import unittest
import os.path as path

from src import Entity
from src import Authenticator

class TestEntities(unittest.TestCase):
    def setUp(self):
        test_path = path.abspath(path.curdir)+'/tests/'
        test_data_files = os.listdir(path=test_path+'test_data/')
        self.test_json = {}
        for test_file in test_data_files:
            if test_file.find('marvel') > -1:
                key = test_file.split('.')[0].split('-')[1]
                self.test_json[key] = json.load(open(test_path+'/test_data/'+test_file))
        self.characters = self.test_json['character']['data']['results']

    def test_character_id(self):
        entity = Entity('character', self.characters[0])
        self.assertEqual(entity.get('id'), 1011334)
    
    def test_character_name(self):
        entity = Entity('character', self.characters[1])
        self.assertEqual(entity.get('name'), "A-Bomb (HAS)")

    def test_character_entity_summary_objects(self):
        entity = Entity('character', self.characters[0])
        list_of_comics_in_which_character_appears=[21366,24571,21546,21741,
                    21975,22299,22300,22506,8500,10223,10224,10225]
        self.assertEqual(entity.get('comics'),
                    list_of_comics_in_which_character_appears)

if __name__ == '__main__':
    unittest.main()