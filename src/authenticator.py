"""Authenticator.

This module allows the user to easily build authentication string that is used 
in the request string for the API.

The class Authenticator accepts two methods:
    *get_auth_string() - returns the authentic string
    *authenticated() - returns whether the user is authenticated or not

"""

import datetime
import hashlib
import random


#TODO delete these before release
PUBLIC_KEY = '9b6d7545e698ec76a8673df57089edbc'
PRIVATE_KEY = 'd55e975ae3c3a0e3041d7f8688e126c3f0d517dc'

class Authenticator():
    """Class to represent Authenticator object.

    Parameters:
            public_key: The users given public key(given by Marvel)
            private_key: The users given private key(given by Marvel)

    """

    def __init__(self, public_key: str, private_key: str):
        """Constructor.

        Initiates the private and private keys.

        Parameters:
            public_key: The users given public key(given by Marvel)
            private_key: The users given private key(given by Marvel)

        """
        self.__pub_key = public_key
        self.__pri_key = private_key

    def get_auth_string(self) -> str:
        """Get authentication string.

        According to the spec at developer.marvel.com build an authentication
        string by:
            Choosing a timestamp then using md5 hash the timestamp private key
            and public key.

            Build a string by concatinating timestamp + public key + hash

        return:
            Authentication string.

        """
        today = datetime.datetime.today()
        date = ''.join(str(today.date()).split('-'))
        time = ''.join(
            str(today.time()).split('.')[0].split(':'))

        
        time_stamp = date + time
        string = time_stamp + self.__pri_key + self.__pub_key
        
        encoded_string = string.encode(encoding='UTF-8', errors='strict')
        hasher = hashlib.md5()
        hasher.update(encoded_string)

        auth_string = 'ts='+time_stamp
        auth_string += '&apikey='+self.__pub_key
        auth_string += '&hash='+hasher.hexdigest()
        return auth_string