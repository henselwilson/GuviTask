import csv
import ForgotPassword

def wrongPasswrdAction():
    action=input("Enter Retry/Forgot: ")
    if action.lower()=="retry":
        return 2
    elif action.lower()=="forgot":
        ForgotPassword.ForgotPwdActions()
    else:
        print("Invalid Entry")
        wrong_passVal=wrongPasswrdAction()
    return wrong_passVal

class ExistingUser:
    def __init__(self,email,password):
        self.email=email
        self.password=password
    def wrong_email_Action(self):
        wrong_email_actionKey = input("Enter Retry/Register: ")
        if wrong_email_actionKey.lower() == "register":
            return 1
        elif wrong_email_actionKey.lower() == "retry":
            return 2
        else:
            print("Invalid input")
            wrong_MailVal=self.wrong_email_Action()
            return wrong_MailVal


    def Login(self):
        log_handle = open("emailDetails.csv", "r")
        databRead = csv.DictReader(log_handle)
        datab_row_Read = list(databRead)
        for row in datab_row_Read:
            if row["email"] == self.email:
                if row["password"] == self.password:
                    print("You have logged in Successfully. Welcome to this website")
                else:
                    print("The password you entered is incorrect")
                    print(
                        "Do you want to retry Logging in with a different password or have you forgotten the password?")
                    wrong_passVal = wrongPasswrdAction()
                    return wrong_passVal
                log_handle.close()
                break
        else:
            print("""
The mail ID you have entered is incorrect.
Please Check the email ID you have entered and try again if you ara an existing user.
If you are a new user Register yourself first""")
            wrong_MailVal=self.wrong_email_Action()
            return wrong_MailVal