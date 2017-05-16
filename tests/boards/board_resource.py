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
        create_board_result = self.create_new_board('Python test create new board',
                                                    'This board has been made using the api')

        self.assertEqual(200, create_board_result['status_code'])

        self.delete_board(create_board_result['board_id'])

    # def test_can_update_board_name(self):

    def create_new_board(self, name, description):
        new_trello_board = {
            'name': name,
            'desc': description
        }
        response = requests.post(f'{self.TRELLO_BASE_URL}/boards?token={TOKEN}', json=new_trello_board)

        return {
            'board_id': response.json()['id'],
            'status_code': response.status_code
        }

    def delete_board(self, board_id):
        response = requests.delete(
            f'{self.TRELLO_BASE_URL}/boards/{board_id}?token={TOKEN}')

        self.assertEqual(response.status_code, 200)