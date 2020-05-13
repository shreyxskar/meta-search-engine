import sqlite3

conn = sqlite3.connect('test.db')
stmt="insert into products values(\"%s\",\"%s\",\"%s\")"%()





print("Opened database successfully")

stmt="delete from products where name is \"%s\";"%"Mobile"
conn.execute(stmt)
print("Data Deleted!")

stmt="select name, price, website from products"
cursor=conn.execute(stmt)
for row in cursor:
    print(row[0],row[1],row[2])
print("Done")

'''
stmt="insert into products values(\"%s\", \"%s\", \"%s\");"%("Mobile","Price","Website")

conn.execute(stmt)
print("Data inserted!")

conn.execute(stmt)
print("Data inserted!")

conn.execute(stmt)
print("Data inserted!")


stmt="select name, price, website from products"
cursor=conn.execute(stmt)
for row in cursor:
    print(row[0],row[1],row[2])
              


#stmt="delete from products where name is \"%s\";"%"Mobile"

#conn.execute(stmt)
print("Data Deleted!")

stmt="select name, price, website from products"
cursor=conn.execute(stmt)
for row in cursor:
    print(row[0],row[1],row[2])
print("Done")'''
