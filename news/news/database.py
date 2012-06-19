#!/usr/bin/env python   
#-*- coding: utf-8 -*-   
###################################   
# @author oangeor   
# @created 2010-01-17   
##################################   
#MySQLdb 示例   
#   
##################################   
import MySQLdb   
class CMySQL:
    host=''
    user=''
    passwd=''
    dbname=''
    cursor=None
    def __init__(self,host,user,passwd,dbname):
        self.host=host
        self.user=user
        self.passwp=passwd
        self.dbname=dbname
        
    def link(self):
        
        try:
            conn = MySQLdb.connect(host=self.host, user=self.user,passwd=self.passwd)   
        except:
            print '数据库失败1'
        try:
            self.cursor = conn.cursor()
            self.cursor.execute('create database if not exists %s' %self.dbname) 
            conn.select_db(self.dbname);
            #新建表
            #self.cursor.execute("create table newstb(id int primary key, school varchar(100),title varchar(100),link varchar(100),addtime varchar(100))  ")    
        except:
            print '数据库失败2'
            
    def sql_insert(self,tbname,values):
        #self.cursor.execute("set names 'utf8'")
        #if len(values)>1:
        print values[0]
        self.cursor.execute('insert into %s'%tbname +' values(%s,%s,%s,%s,%s) ' ,values[0]);
        #else:
         #   print values
          #  self.cursor.executemany('insert into %s'%tbname +' values(%s,%s,%s,%s,%s) ' ,values);
        #pass
    def close():
        self.cursor.close();    
    def sql_query(self,sql):
        count = self.cursor.execute(sql)  
        print '总共有 %s 条记录' %count
        results = self.cursor.fetchall()
        return results; 
    def sql_update(sql):
        self.cursor.execute(sql) 
        #for r in results:  
        #    print r[0],r[1],r[2],r[3],r[4]      
if __name__=='__main__':
    host='localhost'
    user='root'
    passwd=''
    dbname='news'
    sql=CMySQL(host,user,passwd,dbname)
    sql.link()
    values=[]
    values.append((11211201,'哈哈','[呵呵]','link','time'))
    #values.append((1111022,'HIT','title','link','time'))
    sql.sql_insert('newstb',values)
    #sql.sql_query()
