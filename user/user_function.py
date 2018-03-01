import unittest

class User:
    # This is user infor, the users are stored in a dictionary
    def __init__(self):
        self.users = {}

    def create_user(self,userName):
        if userName == None or userName == "":
            return "Invalid userName"
        if userName not in self.users: # The userName is unique
            self.users[userName] = 0 #Initializa as a number 0, we can set it as a list to store password and other information.
            print(userName,"create successfully")
            return self.users
        else:
            return "Username already exist, please try another one."

    def delete_user(self, userName):
        if userName == None or userName =="":
            return "Invalid userName"
        if userName in self.users: # The userName is unique
            del self.users[userName] #Initializa as a number 0, we can set it as a list to store password and other information.
            print(userName,"delete successfully")
            return self.users
        else:
            return "Username doesn't exist, please try another one."
if __name__ == "__main__":
    u = User()
    print(u.create_user("adad"))

