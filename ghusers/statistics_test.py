#-*- coding=utf-8 -*-
'''
@info 统计数据库中观海用户信息的测试文件
@author oangeor<oangeor@gmail.com>
@date 2012-06-17
@todo 最近还要考试，测试文件只写了一点，没有规格化，考试完之后再修改
'''
from pymysql import PyMysql
from config import HOST,USER,PASSWD,DATABASE



testdb=PyMysql(HOST,USER,PASSWD,DATABASE)
'''
sexstr=list()
sexstr.append('select * from users where sex="男"')
sexstr.append('select * from users where sex="女"')
sexstr.append('select * from users where sex="保密"')
print sexstr
for sqlstr in sexstr:
    result=testdb.query(sqlstr)
    print len(result)
'''
#strsql='select * from users where useronlie>%d'

#onlinesql=list()
#onlinesql.append()
'''
#在线时长统计

for i in range(0,15):
    i*=1000
    sqlstr='select * from users where useronline>%d and useronline<%d' %(i-1000,i)    
    result=testdb.query(sqlstr)
    print i,'\t',len(result)
    #print sqlstr
'''

'''
#注册日期统计

for i in range(2000,2013):
    sqlstr='select *  from users where regtime >="%d-01-01 00:00:00" and regtime <="%d-01-01 00:00:00" ' %(i,i+1);
    #print sqlstr
    result=testdb.query(sqlstr)
    print '\t',len(result)
'''

'''
#注册日期统计

for i in range(0,10):
    i*=10
    sqlstr='select *  from users where topic>=%d and topic <%d ' %(i,i+10);
    #print sqlstr
    result=testdb.query(sqlstr)
    print '\t',len(result)
'''
#注册日期统计

for i in range(0,10):
    i*=10
    sqlstr='select *  from users where topic>=%d and topic <%d ' %(i,i+10);
    #print sqlstr
    result=testdb.query(sqlstr)
    print '\t',len(result)

