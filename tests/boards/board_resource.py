import unittest
import requests


class BoardResource(unittest.TestCase):
    def test_can_create_new_board(self):
        response = requests.get('https://www.google.com')
        self.assertEqual(200, response.status_code)
