import csv

def ForgotPwdActions():
    email = input("Enter your mail ID: ")
    ForgotPwd_handle=open("emailDetails.csv","r")
    databRead = csv.DictReader(ForgotPwd_handle)
    datab_row_Read = list(databRead)
    for row in datab_row_Read:
        if row["email"] == email:
            print("The password for your Email {} is {}".format(row['email'], row['password']))
            break
    else:
        print("""
The mail ID you have entered is incorrect.
Please Check the email ID you have entered and try again.""")
        wrongEmailAction()

def wrongEmailAction():
    wrong_email_actionKey = input("Enter Retry/Exit: ")
    if wrong_email_actionKey.lower() == "retry":
        ForgotPwdActions()
    elif wrong_email_actionKey == "Exit":
        pass
    else:
        print("Invalid input")
        wrongEmailAction()