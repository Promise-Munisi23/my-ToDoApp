import unittest
from unittest.mock import patch
from Adding import *
from sign_up import *
from deleting import *


class TestTodoApp(unittest.TestCase):

    def test_add_todo(self):
        items = "shopping"
        date = "2024-03-12"

        with patch('builtins.print') as mocked_print:
            add_todo(items, date)
            mocked_print.assert_called_with('items added to the todo successfully!')

class TestUserAuthentication(unittest.TestCase):

    @patch('builtins.input', side_effect=['nnn@example.com', 'testing password'])
    def test_save_info_in_csv(self, mocked_input):
        save_info_in_csv('nnn@example.com', 'testing password')
        users = read_info_in_csv()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['user_email'], 'nnn@example.com')
        self.assertEqual(users[0]['user_password'], 'testing password')

    @patch('builtins.input', side_effect=['tyt@example.com', 'testing password'])
    def test_authenticate_user_valid(self, mocked_input):
        self.assertFalse(authenticate_user('tyt@example.com', 'testing password'))

    @patch('builtins.input', side_effect=['wrong@example.com', 'non-existent password'])
    def test_authenticate_user_invalid(self, mocked_input):
        self.assertFalse(authenticate_user('wrong @example.com', 'non-existent password'))

if __name__ == '__main__':
    unittest.main()

