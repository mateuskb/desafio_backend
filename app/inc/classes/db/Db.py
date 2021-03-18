import sys, os
import psycopg2
from psycopg2 import extras

BASE_PATH = os.path.abspath(__file__+ '/../../../../')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts

class DbLib:

    def __init__(self, sgbd='pgsql'):
        if sgbd in consts.SGBDS:
            self.sgbd = sgbd
        else:
            self.sgbd = ''
    
    def connect(self, db=consts.GESTME_DB):
        if self.sgbd == 'pgsql':
            try:
                conn = psycopg2.connect(host=db['hostname'], user=db['username'], password=db['password'], dbname=db['database'])
                return conn
            except:
                return False
        else:
            return False
