# Anonymous version of the email generation

import random
import smtplib, ssl
from email.message import EmailMessage
import sys

'''
Simple script that generates a Secret Santa pool
- Enter number of people participating
- Enter everyone's name
- Enter everyone's email address
'''

# Ask how many people participate
# According to this, store N people's names
# Assign to each person another person randomly

# Secret Santa definition #



class Santa(object):
    def __init__(self, usr, pw):
        self.usr = usr 
        self.pw = pw
        self.nb_ppl = 0
        self.list_ppl = []
        self.email_dict = dict()
        self.secret_dict = dict()
    
    def set_number(self):
        self.nb_ppl = int(input("How many people are participating to the Secret Santa ? --> "))
    
    def set_names(self):
        for i in range(self.nb_ppl):
            self.list_ppl.append(input("Enter person number " + str(i+1) + "'s name --> "))

    def set_emails(self):
        for elem in self.list_ppl:
            self.email_dict[elem] = input("Enter " + elem + "'s EMAIL --> ")

    def gen_secrets(self):
        for elem in self.list_ppl:
            list_match = self.list_ppl.copy()
            list_match.remove(elem)
            secret_santa = random.choice(list_match)
            self.secret_dict[elem] = secret_santa
            list_match.remove(secret_santa)
    
    def send_emails(self):
        mail_from = self.usr
        mail_password = self.pw

        # Send the mail
        for elem in self.list_ppl:
            msg = EmailMessage()
            msg.set_content("Hello " + elem + ", your secret santa is : " + secret_dict[elem])
            msg["Subject"] = "Secret Santa"
            msg["From"] = mail_from
            msg["To"] = self.email_dict[elem]
            context=ssl.create_default_context()

            with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
                smtp.starttls(context=context)
                smtp.login(msg["From"], mail_password)
                smtp.send_message(msg)

if __name__ == '__main__':
    ss = Santa()
    ss.set_number()
    ss.set_names()
    ss.set_emails()
    ss.gen_secrets()
    ss.send_emails()