'''
author : Erwin Lejeune <erwin.lejeune15@gmail.com>
date : 23 Nov 2019
repo : https://github.com/Guilyx/secret-santa
'''
import random
import smtplib, ssl
from email.message import *
import imaplib

class Flush(object):
    def __init__(self, usr, pw, n_deleted):
        print("\nConnecting to the GMAIL server...")
        self.box = imaplib.IMAP4_SSL("imap.gmail.com") # connecting to gmail boxer
        self.usr = usr
        self.pw = pw
        self.n_deleted = n_deleted


    def connectImap(self):
        connect = self.box.login(self.usr, self.pw)
        print(connect)


    def checkListLabels(self):
        print(self.box.list())


    def deleteSentMails(self):
        print("Deleting all sent emails...")
        self.box.select('"[Gmail]/Sent Mail"')
        typ, data = self.box.search(None, 'ALL')

        i = 0
        for num in data[0].split():
            if (i > self.n_deleted + 1):
                break
            else:
                self.box.store(num, '+FLAGS', '\\Deleted')
            i += 1

        self.box.expunge()
    
    # Needed if your Gmail parameters stores deleted emails in the trash
    def cleanTrash(self):
        print("Emptying Trash & Expunge...")
        self.box.select('[Gmail]/Trash')  # select all trash
        self.box.store("1:*", '+FLAGS', '\\Deleted')  #Flag all Trash as Deleted
        self.box.expunge()


    def logout(self):
        print("Closing imap and logging out...")
        self.box.close()
        self.box.logout()


class Santa(object):
    def __init__(self, usr, pw):
        self.usr = usr 
        self.pw = pw
        self.nb_ppl = 0
        self.list_ppl = []
        self.email_dict = dict()
        self.secret_dict = dict()
        
    
    def set_number(self, setN = None):
        if (setN == None):
            self.nb_ppl = int(input("\nHow many people are participating to the Secret Santa ? --> "))
        else:
            self.nb_ppl = setN


    def set_names(self, list_names = None):
        if (list_names == None):
            for i in range(self.nb_ppl):
                self.list_ppl.append(input("\nEnter person number " + str(i+1) + "'s name --> "))
        else:
            self.list_ppl = list_names[0:self.nb_ppl]


    def set_emails(self, email_dict = None):
        if (email_dict == None):
            for elem in self.list_ppl:
                self.email_dict[elem] = input("\nEnter " + elem + "'s EMAIL --> ")
        else:
            self.email_dict = email_dict

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
            msg.set_content("Hello " + elem + ", your secret santa is : " + self.secret_dict[elem])
            msg["Subject"] = "Secret Santa"
            msg["From"] = mail_from
            msg["To"] = self.email_dict[elem]
            context=ssl.create_default_context()

            with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
                smtp.starttls(context=context)
                smtp.login(msg["From"], mail_password)
                smtp.send_message(msg)

    def flush_emails(self):
        ##### Flushing #####
        flush_sent = Flush(self.usr, self.pw, self.nb_ppl)
        flush_sent.connectImap()
        flush_sent.deleteSentMails()
        flush_sent.cleanTrash()
        flush_sent.logout()


if __name__ == '__main__':
    ss = Santa("toto@tati.tata", "prout")
    ss.set_number()
    ss.set_names()
    ss.set_emails()
    ss.gen_secrets()
    ss.send_emails()
    ss.flush_emails()