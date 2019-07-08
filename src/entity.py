"""Entity.

This module implements the class Entity as given by the Marvel API
(https://developer.marvel.com).

The class is implemented as a magic class with its attributes
automatically created at instantialisation

"""
import json


class Entity():
    def __init__(self, entity_type: str, attributes: dict):
        self.__dict__ = {}
        self.entity_type = entity_type
        self.__init_attribs(attributes)

    def __init_attribs(self, attributes: dict):
        dictionary_type_attributes = ['comics', 'series', 'stories',
                                      'events', 'urls']
        images = ['thumbnail', 'images']
        entity_summary_list = ['collectedIssues', 'collections', 'variants']

        for key, value in attributes.items():

            if key not in dictionary_type_attributes:
                self.__dict__[key] = value

            elif key in images:
                self.__dict__[key] = []
                if key == 'thumbnail':
                    self.__process_image(key, value)
                else:
                    self.__process_image_list(key, value)

            elif key in ['urls', 'dates', 'prices']:
                self.__dict__[key] = {}
                for item in value:
                    self.__dict__[key][item['type']] = item[key[:-1]]

            else:
                self.__dict__[key] = []
                if (key == 'series' and self.entity_type == 'comic')\
                        or key == 'originalIssue':
                    self.__process_entity_summary(key, value)

                elif key in (entity_summary_list + dictionary_type_attributes):
                    self.__process_resource_list(key, value['items'])

    def __process_image(self, key: str, image: dict):
        image_uri = image['path'] + 'detail' + '.' + image['extention']
        self.__dict__[key].append(image_uri)

    def __process_image_list(self, key: str, images: list):
        for image in images:
            self.__process_image(key, image)

    def __process_entity_summary(self, key: str, attribute: dict):
        # split resourceURI and get the last part of the string
        item_id = int(attribute['resourceURI'].split('/')[-1])
        self.__dict__[key].append(item_id)

    def __process_resource_list(self, key: str, items: list):
        for item in items:
            self.__process_entity_summary(key, item)

    def get(self, attribute: str):
        invalid_argument = 'Attribute {!r} is not a member of Entity'.format(
            attribute)
        if attribute not in self.__dict__:
            raise AttributeError(invalid_argument)
        else:
            return self.__dict__[attribute]

    def __eq__(self, other):
        for key, value in self.__dict__.items():
            if value != other.__dict__[key]:
                return False
        return True
