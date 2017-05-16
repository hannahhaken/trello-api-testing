import requests
import unittest
from tests.configuration.trello_token import TOKEN


class BoardResource(unittest.TestCase):
    TRELLO_BASE_URL = 'https://api.trello.com/1'

    def test_can_view_the_test_board(self):
        # GIVEN
        board_id = 'PJ0OHfNl'

        # WHEN
        response = requests.get(
            f'{self.TRELLO_BASE_URL}/boards/{board_id}/lists?token={TOKEN}')

        # THEN
        trello_columns = response.json()

        self.assertEqual(trello_columns[0]['id'], '5772e42314ea86e7d305bade')

    def test_can_create_new_board(self):
        # GIVEN
        new_trello_board = {
            'name': 'Python test create board',
            'desc': 'This board has been made using the api'
        }
        '5918887368d46016929ec940'
        # WHEN
        response = requests.post(f'{self.TRELLO_BASE_URL}/boards?token={TOKEN}', json=new_trello_board)

        id_of_created_board = response.json()['id']

        # THEN
        self.assertEqual(200, response.status_code)

        self.delete_board(id_of_created_board)

    def delete_board(self, board_id):
        response = requests.delete(
            f'{self.TRELLO_BASE_URL}/boards/{board_id}?token={TOKEN}')

        self.assertEqual(response.status_code, 200)
