
# Marvel API


Towel Stuff provides such and such and so and so. You might find
it most useful for tasks involving <x> and also <y>. Typical usage
often looks like this::

Marvel Api provide a  wrapper for the [Marvel API](https://developer.marvel.com).
You might find it most useful for tasks involving fetching and using elements from
this api without having to explicitly write out the request. ::

    #!/usr/bin/python3

    from marvelapi import MarvelAPI

    public_key = 'Key given by marvel at registration'
    private_key = 'Key given by marvel at registration'

    API = MarvelAPI(public_key, private_key)

    characters = API.get_characters_where(name="spider-man")
    for character in characters:
        print(character.get('description'))

# Entities

The API has 6 entities which are.

* characters
* comics
* creators
* series
* stories
* events

## Gets


Each entity has two get methods:

1. ``*entity*_get_by_id(id: int) -> Entity``

2. ``get_*entity*_where(**kwargs) -> List of entities``

* The ``**kwargs`` are key word arguments where each key is a possible search parameter for that entity

# Possible Search parameters

[This](./docs/search_params.md) is a comprehensive list of all possible search parameters and their types
