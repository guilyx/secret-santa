import imaplib
from lib.santa_gen import Santa

'''
Simple script that deletes your sent emails

- Could add other methods for other boxes
- Could delete last x mails
- Could delete emails since t time
'''

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
    
    def selectLastN(self):
        temp_string = [str(i) for i in range(self.n_deleted)]
        new_string = ''

        for elem in temp_string:
            new_string += elem + ' '

        new_string = new_string[:-1]
        res = [new_string]

        return res

    def deleteSentMails(self):
        print("Deleting all sent emails...")
        self.box.select('"[Gmail]/Sent Mail"')
        filter = self.selectLastN()
        typ, data = self.box.search(None, filter)

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
        print("Closing imap and logging out...")
        self.box.close()
        self.box.logout()
