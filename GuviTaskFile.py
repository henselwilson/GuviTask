def RegistrationActions():
    email = input("Enter your new mail ID")
    pwd = input("Enter your Password")
    NewUser = MailCheck(email, pwd)
    mailScore = NewUser.mailCheck()
    pass_score = NewUser.passCheck()
    if mailScore == 5 and pass_score == 5:
        addUser = Add_New_User(email, pwd)
        addUser.register_user()
    else:
        print(
            "You Email/Password doesn't comply with the current conditions. Please read the Necessary requirements for email and password")

def LoginActions():
    email = input("Enter your new mail ID")
    pwd = input("Enter your Password")
    Login_det=ExistingUser(email,pwd)
    Login_det.Login()

class MailCheck:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def mailCheck(self):
        mailScore=0
        split_at=self.username.split('@')
        split_dot=self.username.split('.')

        if len(split_at)==2:
            mailScore+=1
        else:
            return mailScore
        if len(split_dot)==2:
            mailScore+=1
        else:
            return mailScore
        if self.username.index('.')>(self.index('@')+1):
            mailScore+=1
        else:
            return mailScore
        if len(split_at[0])>=1:
            mailScore+=1
        else:
            return mailScore
        special_Char="'[@_!$%^&*()<>?/\|}{~:]#\""
        if split_at[0][0] not in(special_Char):
            mailScore+=1
        else:
            return mailScore

        return mailScore

    def passCheck(self):
        passScore=0
        if len(self.password)>5 and len(self.password<16):
            passScore+=1
        else:
            return passScore
        special_Char = "'[@_!$%^&*()<>?/\|}{~:]#\""
        for i in special_Char:
            if i in self.password:
                passScore+=1
                break
        else:
            return passScore
        for i in self.password:
            try:
                j=int(i)
                passScore+=1
                break
            except:
                pass
        else:
            return passScore

        for i in self.password:
            if i.isupper():
                passScore+=1
                break
        else:
            return passScore

        for i in self.password:
            if i.islower():
                passScore+=1
                break
        else:
            return passScore

        return passScore


def invalidEntryAction():
    action = input("Do you want to Login (Yes/No)")
    if action.lower() == "yes":
        LoginActions()
    elif action.lower() == "no":
        return
    else:
        invalidEntryAction()


class Add_New_User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_user(self):
        handle = MongoClient(
            'mongodb://spidey:Spidey123@wilson-shard-00-00.e39um.mongodb.net:27017,wilson-shard-00-01.e39um.mongodb.net:27017,wilson-shard-00-02.e39um.mongodb.net:27017/?ssl=true&replicaSet=atlas-miz7gu-shard-0&authSource=admin&retryWrites=true&w=majority')
        datab = handle['UserData']
        collect = datab['Email_Details']
        isExisting = collect.find({'email': self.email})
        if len(isExisting) == 0:
            entry = {'email': self.username, 'password': self.password}
            collect.insert_one(entry)
            print("Successfully registered New User. Login to Continue")
        else:
            print("This Account already Exists")
            invalidEntryAction()

def wrongPasswrdAction():
    action=input("Enter Retry/Forgot")
    if action=="retry":
        LoginActions()
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
            RegistrationActions()
        elif wrong_email_actionKey.lower() == "retry":
            LoginActions()
        else:
            print("Invalid input")
            self.wrong_email_Action()

    def Login(self):
        log_handle=MongoClient('mongodb://spidey:Spidey123@wilson-shard-00-00.e39um.mongodb.net:27017,wilson-shard-00-01.e39um.mongodb.net:27017,wilson-shard-00-02.e39um.mongodb.net:27017/?ssl=true&replicaSet=atlas-miz7gu-shard-0&authSource=admin&retryWrites=true&w=majority')
        userData=log_handle['UserData']
        emailDetails=userData['Email_Details']

        result=emailDetails.find({'email':self.email})
        if len(result)==0:
            print("""
The mail ID you have entered is incorrect.
Please Check the email ID you have entered and try again if you ara an existing user.
If you are a new user Register yourself first""")
            self.wrong_email_Action()
        else:
            if result['password']==self.password:
                print("You have logged in Successfully. Welcome to this website")
            else:
                print("The password you entered is incorrect")
                print("Do you want to retry Logging in with a different password or have you forgotten the password?")
                wrongPasswrdAction()

def ForgotPwdActions():
    email = input("Enter your new mail ID")
    ForgotPwd_handle=MongoClient('mongodb://spidey:Spidey123@wilson-shard-00-00.e39um.mongodb.net:27017,wilson-shard-00-01.e39um.mongodb.net:27017,wilson-shard-00-02.e39um.mongodb.net:27017/?ssl=true&replicaSet=atlas-miz7gu-shard-0&authSource=admin&retryWrites=true&w=majority')
    userData = ForgotPwd_handle['UserData']
    emailDetails = userData['Email_Details']

    result = emailDetails.find({'email': email})
    print("Your password for yu Email {} is {}".format(result['email'],result['password']))

print("""
Geetings!!! Welcome to this website. 
Enter \'Register\' to register yourself if you are a new user.
Enter \'Login\' to log into your account.
""")


action=input("Enter Register/Login: ")

if action.lower()=="register":
    RegistrationActions()
elif action.lower()=="login":
    LoginActions()