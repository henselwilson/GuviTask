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
        if self.username.index('.')>(self.username.index('@')+1):
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
        if len(self.password)>5 and len(self.password)<16:
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