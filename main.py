from lib.email_flush import Flush
from lib.santa_gen import Santa
import sys


if __name__ == '__main__':
    args = dict([arg.split('=') for arg in sys.argv[1:]])


    ss = Santa(args['mail'], args['pw'])
    flush_sent = Flush(args['mail'], args['pw'])

    ss.set_number()
    ss.set_names()
    ss.set_emails()
    ss.gen_secrets()
    ss.send_emails()

    flush_sent.connectImap()
    flush_sent.deleteSentMails()
    flush_sent.logout()
