import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.email_flush import Flush
from lib.santa_gen import Santa

class EmailTest:
    def __init__(self):
        self.ss = Santa("totoletontontesteur@gmail.com", "testonetwoonetwo")
        self.flush = Flush("totoletontontesteur@gmail.com", "testonetwoonetwo")
    
    def test_nb_people(self):
        assert self.ss.nb_ppl > 0
    
    def test_people(self):
        assert len(self.ss.list_ppl) > 0
        assert len(self.ss.list_ppl) == self.ss.nb_ppl

    

