import sqlite3

conn = sqlite3.connect('ProductDetails.db')

print("Opened database successfully")
'''
stmt="select * from products order by name asc; "
cursor=conn.execute(stmt)
for row in cursor:
    tpl=(row[0],row[1],row[2])
    print(tpl)

print("Printed")'''

print("Table created!")
str="S h r e y a s k a r"
print(str.replace(' ','').replace('e','3'))

c=conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hel4566lo';")

if c.fetchone() is None:
    print("No table ->%s"%"hel4566lo")
else:
    print("Table -> %s"%"hel4566lo")

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
if c.fetchone() is None:
    print("No table -> %s"%"products")
else:
    print("Table -> %s"%"products")

'''if not a:
    print("Yes")
else:
    print("No")
stmt="drop table napa"
conn.execute(stmt)
print("Donw here")
'''
