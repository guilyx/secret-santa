import imaplib
import sys

'''
Simple script that deletes your sent emails

-email: Gmail email
-pw: gmail pw
'''

class Flush(object):
    def __init__(self, usr, pw):
        print("Connecting to the GMAIL server...")
        self.box = imaplib.IMAP4_SSL("imap.gmail.com") # connecting to gmail boxer
        self.usr = usr
        self.pw = pw

    def connectImap(self):
        connect = self.box.login(self.usr, self.pw)
        print(*connect)

    def checkListLabels(self):
        print(*self.box.list())

    def deleteSentMails(self):
        print(*self.box.select('"[Gmail]/Sent Mail"'))
        typ, data = self.box.search(None, 'ALL')
        for num in data[0].split():
            self.box.store(num, '+FLAGS', '\\Deleted')
        self.box.expunge()
    
    # Needed if your Gmail parameters stores deleted emails in the trash
    def cleanTrash(self):
        print("Emptying Trash & Expunge...")
        self.box.select('[Gmail]/Trash')  # select all trash
        self.box.store("1:*", '+FLAGS', '\\Deleted')  #Flag all Trash as Deleted
        self.box.expunge()

    def logout(self):
        self.box.close()
        self.box.logout()

if __name__ == '__main__':
    flush_sent = Flush()
    flush_sent.connectImap()
    flush_sent.deleteSentMails()
    flush_sent.logout()
