import sqlite3

conn=sqlite3.connect("tripAdvisor.db")
stmt="DROP TABLE HOT_REV;"
conn.execute(stmt)
print("Deleted")
