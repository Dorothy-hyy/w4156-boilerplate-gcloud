import unittest
from user_function import User
from enum import Enum, auto

"""
class returntype(Enum):
    "Invalid userName" = auto()
    "Username already exist, please try another one." = auto()
    "Username doesn't exist, please try another one." = auto()
"""

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User()
    
    def test_create_user(self):
        success_case = [
            "abc",
            "def",
            "ghi"
        ]
        exist_error_case = [
            "abd",
            "def"
        ]
        none_error = [""]
        num = 0 # imitate the number of user in User database
        for case in success_case:
            res = self.user.create_user(case)
            num += 1
            self.assertEqual(len(res),num)
        for case in exist_error_case:
            res = self.user.create_user(case)
            self.assertEqual(res,"Username already exist, please try another one.")
        for case in none_error:
            res = self.user.create_user(case)
            self.assertEqual(res,"Invalid userName")
    def test_delete_user(self):
        pass
               
if __name__ == '__main__':
    unittest.main()    
