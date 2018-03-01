import unittest
from user_function import User

class returntype(Enum):
    "Invalid userName" = auto()
    "Username already exist, please try another one." = auto()
    "Username doesn't exist, please try another one." = auto()

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
            self.assertEqual(res,num)
        for case in exist_error_case:
            res = self.user.create_user(case)
            self.assertEqual(res, returntype(2))
        for case in none_error:
            res = self.user.create_user(case)
            self.assertEqual(res, returntype(1))
       
if __name__ == '__main__':
    unittest.main()    
          
