from lib.email_flush import Flush
from lib.santa_gen import Santa


if __name__ == '__main__':
    ss = Santa()
    flush_sent = Flush()

    ss.set_number()
    ss.set_names()
    ss.set_emails()
    ss.gen_secrets()
    ss.send_emails()

    flush_sent.connectImap()
    flush_sent.deleteSentMails()
    flush_sent.logout()
