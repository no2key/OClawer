#-*- coding: utf-8 -*-

import re,time,datetime
import config
#from lib.SQLite import SQLite
import database

def log(mesg):
    try:
        print mesg.encode("utf-8")
    except:
        print mesg



def get_last_title():
    sql=database.CMySQL('localhost','root','','news')
    sql.link()
    strid=sql.sql_query('select * from posttb ')
    print strid[0][0]
def str2date(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    #drop_table()
    get_last_title()
