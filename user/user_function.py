import unittest

class User:
    # This is user infor, the users are stored in a dictionary
    users ={}

    def create_user(userName):
        if userName == None or userName == "":
            return "Invalid userName"
        if userName not in users: # The userName is unique
            users[userName] = 0 #Initializa as a number 0, we can set it as a list to store password and other information.
            print(userName,"create successfully")
            return users
        else:
            return "Username already exist, please try another one."

    def delete_user(userName):
        if userName==None or userName =="":
            return "Invalid userName"
        if userName in users: # The userName is unique
            del users[userName] #Initializa as a number 0, we can set it as a list to store password and other information.
            print(userName,"delete successfully")
            return users
        else:
            return "Username doesn't exist, please try another one."
