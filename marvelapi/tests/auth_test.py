import unittest
from marvelapi import Authenticator


class TestAuthenticator(unittest.TestCase):
    def test_authenticator(self):
        PUBLIC_KEY = '1234'
        PRIVATE_KEY = 'abcd'
        TIME_STAMP = '1'
        auth = Authenticator(PUBLIC_KEY, PRIVATE_KEY, TIME_STAMP)
        self.assertEqual(auth.get_auth_string(),
                         'ts=1&apikey=1234&hash=' +
                         'ffd275c5130566a2916217b101f26150')


if __name__ == "__main__":
    unittest.main()
