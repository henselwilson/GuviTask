import csv

def invalidEntryAction():
    action = input("Do you want to Login (Yes/No)")
    if action.lower() == "yes":
        return 2
    elif action.lower() == "no":
        return
    else:
        invVal=invalidEntryAction()
        return invVal


class Add_New_User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

            
    def register_user(self):
        handle_Read=open("emailDetails.csv","r")
        hanndle_Write=open('emailDetails.csv',"a",newline="")
        databRead=csv.DictReader(handle_Read)
        datab_row_Read=list(databRead)
        for row in datab_row_Read:
            if row["email"] == self.username:
                print("This Account already Exists")
                isLogin=invalidEntryAction()
                handle_Read.close()
                hanndle_Write.close()
                break
        else:
            entry = [self.username, self.password]
            databWriter=csv.writer(hanndle_Write)
            databWriter.writerow(entry)
            print("Successfully registered New User. Login to Continue")
            handle_Read.close()
            hanndle_Write.close()
        return 2