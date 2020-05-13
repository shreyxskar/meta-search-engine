import sqlite3

conn=sqlite3.connect("tripAdvisor.db")
inp=input("Enter keyword : ")
ss=[]
ss.append("%"+inp+"%")
#ss=["%worst%","%bad%experience%","%bad%food%","%bad%room%","%major issue%"]
for k in ss:
    stmt="SELECT distinct * FROM HOT_REV WHERE review like \""+k+"\";"
    res=conn.execute(stmt)
    #print(stmt)
    j=0
    #print("Hotels List")
    for i in res:
        #print(i[0])
        print("Hotel Name :",i[0],"\nReview by :",i[2],"\nDate :",i[3],"\n",i[4],sep="")
        print()
        j+=1
    print(j,"reviews")#,k)

#print(ss)

stmt="SELECT count(distinct hotel_name) from HOT_REV;"
sd=conn.execute(stmt)
for i in sd:
    print(i[0])

print()

'''

2 apps->

1)customer -> search hotels based on their preferences(eg. location, good food)
2)hotelier -> search hotels with bad reviews(eg. bad food, major issue)

*3)self-> perfect ranking for hotels based on review analysis

'''
