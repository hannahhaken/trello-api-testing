import requests
import unittest
from tests.configuration.trello_token import TOKEN


class ListResource(unittest.TestCase):
    TRELLO_BASE_URL = 'https://api.trello.com/1'

    def test_can_create_list(self):
        # GIVEN
        created_board_result = self.create_new_board('can create list', 'description')
        board_id = created_board_result['board_id']

        response = requests.post(f'{ListResource.TRELLO_BASE_URL}/lists?token={TOKEN}', json={
            'name': 'new list',
            'idBoard': board_id
        })

        self.assertEqual(response.status_code, 200)
        self.delete_board(board_id)

    @staticmethod
    def create_new_board(name, description):
        new_trello_board = {
            'name': name,
            'desc': description
        }
        response = requests.post(f'{ListResource.TRELLO_BASE_URL}/boards?token={TOKEN}', json=new_trello_board)

        return {
            'board_id': response.json()['id'],
            'status_code': response.status_code
        }

    def delete_board(self, board_id):
        response = requests.delete(
            f'{ListResource.TRELLO_BASE_URL}/boards/{board_id}?token={TOKEN}')

        self.assertEqual(response.status_code, 200)
