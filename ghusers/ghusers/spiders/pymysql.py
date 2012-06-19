#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   filename:pymysql.py
#   description:the class for mysql operation using MySQLdb
#   create_time:2011/4/3
#   author:fantasy614<fantasy614@gmail.com>

import MySQLdb
#from settings import poi_host,poi_user,poi_passwd,poi_db

class PyMysql():

    # Establich a connection


    def __init__(self,host=None,user=None,passwd=None,db=None):
        if host:
            self.conn = MySQLdb.connect (host=host,
                user=user,
                passwd=passwd,
                db=db,
                charset="utf8")
            self.conn.ping(True)
        else:
            self.conn = MySQLdb.connect (host=poi_host,
                user=poi_user,
                passwd=poi_passwd,
                db=poi_db,
                charset="utf8")
            self.conn.ping(True)
        self.cursor = self.conn.cursor ()
        
    def query(self,sqlstr):
        try:
            self.cursor.execute(sqlstr)
            return self.cursor.fetchall()
        except:
            return
    def insert(self,sqlstr,values):
        print values
        #self.cursor.execute(sqlstr,values)
        '''
        try:
            self.cursor.execute(sqlstr,values)
            #self.conn.commit()
            return True
        except:
            return False         
        '''
    def update(self,sqlstr):
        try:
            self.cursor.execute(sqlstr)
            self.conn.commit()
            return True
        except IOError:
            print IOError
            return False

    def __del__(self):
        self.cursor.close ()
        self.conn.close ()

def dbtest():
    testdb = PyMysql()
    print testdb.query("select * from RSS")
    
if __name__ == '__main__':
    dbtest()
