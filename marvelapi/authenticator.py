"""authenticator.

This module implements the Authenticator class which allows the user to easily
build authentication string that is used in the request string for the API.

The class Authenticator has one methods:
    *get_auth_string() - returns the authentic string

"""

import datetime
import hashlib
import random


# TODO delete these before release


class Authenticator():
    """Class to represent Authenticator object."""

    def __init__(self, public_key: str, private_key: str, time_stamp=None):
        """Constructor.

        Initiates the private and private keys.

        Parameters:
            public_key: The users given public key(given by Marvel)
            private_key: The users given private key(given by Marvel)

        """
        self.__time = time_stamp
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
        time_stamp = self.__get_date_time()
        string = time_stamp + self.__pri_key + self.__pub_key

        encoded_string = string.encode(encoding='UTF-8', errors='strict')
        hasher = hashlib.md5()
        hasher.update(encoded_string)

        auth_string = 'ts='+time_stamp
        auth_string += '&apikey='+self.__pub_key
        auth_string += '&hash='+hasher.hexdigest()
        return auth_string

    def __get_date_time(self):
        if self.__time is None:
            today = datetime.datetime.today()
            date = ''.join(str(today.date()).split('-'))
            time = ''.join(
                str(today.time()).split('.')[0].split(':'))
            return date + time
        else:
            return self.__time
