# MarvelAPI Documentation

This is the documentation for MarvelAPI. A wrapper written for the [Marvel API](https://developer.marvel.com)

## Authenticator

This is a class implemented in [authenticator.py](../src/authenticator.py)

The class accepts the public and private keys as strings on instantiation.

``auth = Authenticator(public_key, private_key)``

According to the Marvel specification all server-side applications that access the
API must pass three parameter:

* ts - A timestamp (or other long string which can change on a request-by-request basis)
    -this wrapper always uses the time stamp.
* hash - A md5 digest of the ts parameter, a private key, and a public key.
* apikey - The public key given to users by Marvel upon registration.

A URI for a valid call, assuming the public key is "1234" and the public key is
"abcd" looks as follows:

``http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150``

The hash value (``hash=ffd275c5130566a2916217b101f26150``) is the md5 digest of 1abcd1234.

The class builds the string starting from the timestamp in this example, the
class would be used to construct the string
``ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150``

This string is returned when the method ``get_auth_string()`` is called.

### Example usage

    auth = Authenticator('1234', 'abcd')
    auth_string = auth.get_auth_string()
    # Assuming the timestamp = 1
    # auth_string is ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150

## Entity

This is the Entity class, as given in the [Marvel Api](https://developer.marvel.com/documentation/entity_types) spec.

The class is a general representation of the following entities in the spec:

* Character
* Comic
* Creator
* Event
* Series
* Story

The ``__init__(self, entity_type:str, attributes:dict)`` method of this class
instantiates the class depending on the keys given in the ``attributes``
dictionary, that is passed in as a parameter.

The attributes are differentiated into a few types given below:

* Normal Types - [int, string, Date]
* Entity Summary Views - Summary views will always contain a resourceURI, which points to the full representation of the referenced entity, and a name, for convenience.
* Resource Lists - Collections of summary views within the context of another entity type.

## Querier
