import unittest
from unittest.mock import patch
from todo_app import add_todo

class TestTodoApp(unittest.TestCase):

    def test_add_todo(self):
        items = "shopping"
        date = "2024-03-12"

        with patch('builtins.print') as mocked_print:
            add_todo(items, date)
            mocked_print.assert_called_with('items added to the todo successfully!')

class TestUserAuthentication(unittest.TestCase):

    @patch('builtins.input', side_effect=['test@example.com', 'testpassword'])
    def test_save_info_in_csv(self, mocked_input):
        save_info_in_csv('test@example.com', 'testpassword')
        users = read_info_in_csv()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['user_email'], 'test@example.com')
        self.assertEqual(users[0]['user_password'], 'testpassword')

    @patch('builtins.input', side_effect=['test@example.com', 'testpassword'])
    def test_authenticate_user_valid(self, mocked_input):
        self.assertTrue(authenticate_user('test@example.com', 'testpassword'))

    @patch('builtins.input', side_effect=['invalid@example.com', 'invalidpassword'])
    def test_authenticate_user_invalid(self, mocked_input):
        self.assertFalse(authenticate_user('invalid@example.com', 'invalidpassword'))

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()