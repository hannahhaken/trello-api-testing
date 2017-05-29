import requests
import unittest
from tests.configuration.trello_token import TOKEN


class BoardResource(unittest.TestCase):
    TRELLO_BASE_URL = 'https://api.trello.com/1'

    def test_can_view_an_existing_board(self):
        # GIVEN
        board_id = 'PJ0OHfNl'

        # WHEN
        response = self.get_board(board_id)

        # THEN
        board = response.json()

        self.assertEqual(board['name'], 'Welcome Board')

    def test_can_create_new_board(self):
        # GIVEN
        created_board_result = self.create_new_board('Python test create new board',
                                                     'This board has been made using the api')

        self.assertEqual(200, created_board_result['status_code'])

        self.delete_board(created_board_result['board_id'])

    def test_can_update_board_name(self):
        # GIVEN
        created_board_result = self.create_new_board('Test can update board name', 'description')
        board_id = created_board_result['board_id']

        response = requests.put(f'{self.TRELLO_BASE_URL}/boards/{board_id}/name?token={TOKEN}', json={
            'value': 'new board name'
        })

        self.assertEqual(response.status_code, 200)

        board = self.get_board(board_id).json()

        self.assertEqual(board['name'], 'new board name')

        self.delete_board(board_id)

    @staticmethod
    def create_new_board(name, description):
        new_trello_board = {
            'name': name,
            'desc': description
        }
        response = requests.post(f'{BoardResource.TRELLO_BASE_URL}/boards?token={TOKEN}', json=new_trello_board)

        return {
            'board_id': response.json()['id'],
            'status_code': response.status_code
        }

    @staticmethod
    def get_board(board_id):
        response = requests.get(f'{BoardResource.TRELLO_BASE_URL}/boards/{board_id}?token={TOKEN}')
        return response

    def delete_board(self, board_id):
        response = requests.delete(
            f'{BoardResource.TRELLO_BASE_URL}/boards/{board_id}?token={TOKEN}')

        self.assertEqual(response.status_code, 200)
