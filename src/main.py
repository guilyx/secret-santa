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

if __name__ == '__main__':
    from lib.qtgui import MyWidget
    
