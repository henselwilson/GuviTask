from MailCheck import MailCheck
from RegisterUser import Add_New_User
from ExistingUser import ExistingUser

def RegistrationActions():
    email = input("Enter your new mail ID: ")
    pwd = input("Enter your Password: ")
    NewUser = MailCheck(email, pwd)
    mailScore = NewUser.mailCheck()
    pass_score = NewUser.passCheck()
    if mailScore == 5 and pass_score == 5:
        addUser = Add_New_User(email, pwd)
        isRegistered=addUser.register_user()
        if isRegistered==2:
            LoginActions()
    else:
        print(
            "You Email/Password doesn't comply with the current conditions. Please read the Necessary requirements for email and password")

def LoginActions():
    email = input("Enter your mail ID: ")
    pwd = input("Enter your Password: ")
    Login_det=ExistingUser(email,pwd)
    isLogged_In=Login_det.Login()
    if isLogged_In==1:
        RegistrationActions()
    elif isLogged_In==2:
        LoginActions()


def FirstAction():
    action=input("Enter Register/Login: ")

    if action.lower()=="register":
        RegistrationActions()
    elif action.lower()=="login":
        LoginActions()
    else:
        print("Invalid Entry")
        FirstAction()


print("""
Geetings!!! Welcome to this website. 
Enter \'Register\' to register yourself if you are a new user.
Enter \'Login\' to log into your account.
""")

FirstAction()