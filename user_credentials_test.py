import unittest
from user_credentials import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Brian', 'Major', 'dead2016') # create user object


    def test__init__(self):
        '''
        Test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.first_name, "Brian")
        self.assertEqual(self.new_user.last_name, "Major")
        self.assertEqual(self.new_user.password, "dead2016")


if __name__ == '__main__':
    unittest.main()
