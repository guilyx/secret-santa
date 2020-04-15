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
from PySide2 import QtWidgets
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.qtgui import MyWidget

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
    
