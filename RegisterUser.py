import csv

def invalidEntryAction():
    action = input("Do you want to Login (Yes/No)")
    if action.lower() == "yes":
        return 2
    elif action.lower() == "no":
        return
    else:
        invalidEntryAction()


class Add_New_User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

            
    def register_user(self):
        handle=open("emailDetails.csv","a+")
        databRead=csv.DictReader(handle)
        datab_row_Read=list(databRead)
        for row in datab_row_Read:
            if row["email"] == self.username:
                print("This Account already Exists")
                invalidEntryAction()
                handle.close()
                break
        else:

            entry = [self.username, self.password]
            databWriter=csv.writer(handle)
            databWriter.writerow(entry)
            print("Successfully registered New User. Login to Continue")
            handle.close()

            