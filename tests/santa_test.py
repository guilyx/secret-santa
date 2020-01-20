import sys
from os import path
from random import randint
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.email_flush import Flush
from lib.santa_gen import Santa

class EmailTest:
    def __init__(self):
        self.ss = Santa("totoletontontesteur@gmail.com", "testonetwoonetwo")
        self.flush = Flush("totoletontontesteur@gmail.com", "testonetwoonetwo")

def test_nb_people():
    test = EmailTest()
    test.ss.set_number(randint(0, 10000000))
    assert test.ss.nb_ppl > 0

def test_people():
    test = EmailTest()
    test.ss.set_number(randint(0, 50))
    list_names = []
    for i in range (test.ss.nb_ppl):
        if (i%2 == 0):
            list_names.append("toto")
        else:
            list_names.append("tata")
    test.ss.set_names(list_names)
    assert len(test.ss.list_ppl) > 0

def test_people_bis():
    test = EmailTest()
    test.ss.set_number(randint(0, 50))
    list_names = []
    for i in range (test.ss.nb_ppl):
        if (i%2 == 0):
            list_names.append("toto")
        else:
            list_names.append("tata")
    test.ss.set_names(list_names)
    assert len(test.ss.list_ppl) == test.ss.nb_ppl

