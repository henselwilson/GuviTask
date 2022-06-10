import csv
import ForgotPassword

def wrongPasswrdAction():
    action=input("Enter Retry/Forgot")
    if action=="retry":
        return 2
    elif action=="forgot":
        ForgotPassword.ForgotPwdActions()
    else:
        print("Invalid Entry")
        wrongPasswrdAction()

class ExistingUser:
    def __init__(self,email,password):
        self.email=email
        self.password=password
    def wrong_email_Action(self):
        wrong_email_actionKey = input("Enter Retry/Register")
        if wrong_email_actionKey.lower() == "register":
            return 1
        elif wrong_email_actionKey.lower() == "retry":
            return 1
        else:
            print("Invalid input")
            self.wrong_email_Action()

    def Login(self):
        log_handle = open("emailDetails.csv", "r")
        databRead = csv.DictReader(log_handle)
        datab_row_Read = list(databRead)
        for row in datab_row_Read:
            if row["email"] == self.username:
                if row["password"] == self.password:
                    print("You have logged in Successfully. Welcome to this website")
                else:
                    print("The password you entered is incorrect")
                    print(
                        "Do you want to retry Logging in with a different password or have you forgotten the password?")
                    wrongPasswrdAction()
                log_handle.close()
                break
        else:
            print("""
            The mail ID you have entered is incorrect.
            Please Check the email ID you have entered and try again if you ara an existing user.
            If you are a new user Register yourself first""")
            self.wrong_email_Action()