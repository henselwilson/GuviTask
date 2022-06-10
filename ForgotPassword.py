
def ForgotPwdActions():
    email = input("Enter your new mail ID")
    ForgotPwd_handle=0
    userData = ForgotPwd_handle['UserData']
    emailDetails = userData['Email_Details']

    result = emailDetails.find({'email': email})
    print("Your password for yu Email {} is {}".format(result['email'],result['password']))