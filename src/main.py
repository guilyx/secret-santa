'''
main script to generate secret santa pool, send emails to participant, flush the sent emails

can't cheat ! hehe

args :
-email: Gmail email
-pw: gmail pw

example : python main.py email=toto@popo.com pw=password
'''

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.santa_gen import Santa



if __name__ == '__main__':
    ##### Getting args ######
    args = dict([arg.split('=') for arg in sys.argv[1:]])

    ##### Generating Mails #####
    ss = Santa(args['mail'], args['pw'])

    ss.set_number()
    ss.set_names()
    ss.set_emails()
    ss.gen_secrets()
    ss.send_emails()
    ss.flush_emails()
    
