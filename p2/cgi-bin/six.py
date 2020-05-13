import csv
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
import sqlite3

q,i=1,0
mFile=open("reviews.csv","r")
with mFile:
    rd=csv.reader(mFile,delimiter=",")
    for row in rd:
        if row:
            if q is 1:
                q=2
                continue
            #print("Review by : %s\n%s\n"%(row[2],row[3]))
            i+=1
            #print()
print(i)

ddb="tripAdvisor.db"
conn=sqlite3.connect(ddb)

stmt='''CREATE TABLE IF NOT EXISTS HOT_REV(HOTEL_NAME VARCHAR(100),HOTEL_LINK VARCHAR(200)
            ,CUSTOMER_NAME VARCHAR(50),REVIEW_DATE VARCHAR(10)
            ,REVIEW VARCHAR(500)    )'''
conn.execute(stmt)
print("Table created!")



mFile=open("reviews.csv","r")

with mFile:
    rdr=csv.reader(mFile,delimiter=",")
    for i in rdr:
        if i:
            if q is 2:
                q=1
                
                continue
            #print(i)
            #stmt=
            conn.execute("INSERT INTO HOT_REV VALUES(?,?,?,?,?)",(i[0],i[1],i[2],i[3],i[4]))
conn.commit()   


stmt='''select sql from sqlite_master where name='HOT_REV';
        '''
conn.execute(stmt)
#print(fff)
'''print("Data printing")
for i in fff:
    print(i)'''
