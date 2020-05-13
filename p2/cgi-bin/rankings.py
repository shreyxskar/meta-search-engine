import sqlite3
import os
import csv

print("Content-type: text/html\r\n\r\n")
printVar="""<html>
<head>
<title>Hotel Rankings Page</title>
<style>
a,a:visited
{
    color:black;
    text-decoration:none;
    transition:0.5s;
}
a:hover
{
    color:white;
}
div.rank
{
    background-color:#00A680;
    border-radius:10px;
    color:black;
    width:%s;
    height:%s;
    padding:15px 15px 15px 15px;
    transition:0.5s;
    margin:10px 10px 10px 10px;
}
div.rank:hover
{
    width:%s
}
span.hofname
{
    color:#00A680;
}
div.rank:hover
{
    color:white;
    span.hofname.color:white;
}
div.secondone
{background:red;
width:40px;}
</style>
</head><body><div class=\"firstone\">"""

dirPath=os.path.dirname(os.path.abspath(__file__))
db=os.path.join(dirPath,"tripAdvisor.db")
conn=sqlite3.connect(db)
#inp=input("Enter keyword : ")
#ss=["%worst%","%unhygienic%","%bad%","%delay%","%problem%","%slow%"]
ss=["%great%","%fast%","%awesome%","%good%","%outstanding%","%best%","%love%"]
newDict={}
#ss.append("%"+inp.replace(' ','%')+"%")
#ss=["%worst%","%bad%experience%","%bad%food%","%bad%room%","%major issue%"]
for k in ss:
    stmt="SELECT * FROM HOT_REV WHERE review like \""+k+"\";"
    res=conn.execute(stmt)
    #print(stmt)
    j=0
    #print("Hotels List")
    for i in res:
        if i[0] in newDict:
            newDict[i[0]]+=1#"Good"#"\n\nReview by : "+i[2]+"\nDate : "+i[3]+"\nReview :\n"+i[4].replace('\\u2026','!')
        else:
            newDict[i[0]]=1#"Good"
#print(len(newDict))
#newDic={}
s1s=["%worst%","%unhygienic%","%bad%","%delay%","%problem%","%slow%","%not%"]
for k2 in s1s:
    stmt="SELECT * FROM HOT_REV WHERE review like \""+k2+"\";"
    res=conn.execute(stmt)
    for i2 in res:
        if i2[0] in newDict:
            newDict[i2[0]]=newDict[i2[0]]-1#+"Bad"
        else:
            newDict[i2[0]]=0#"Bad"
        #"\n\nReview by : "+i[2]+"\nDate : "+i[3]+"\nReview :\n"+i[4].replace('\\u2026','!')
        
#newDict.update(newDic)
'''for i in newDict:
    #print("*******************"+i+"********************")
    print(i,"->",newDict[i])'''
    #print()
#print(len(newDict))
#sort(newDict)
#print("<html><body>")
newVar=1
for w in sorted(newDict, key=newDict.get,reverse=True):
    prevRank,sts=0,""
    sq="SELECT HOTEL_LINK FROM HOT_REV WHERE HOTEL_NAME like \""+w+"\";"
    ll=conn.execute(sq)
    em1=open("ranklist.csv","r")
    em4=open("ranklist1.csv","a")
    with em1:
        prevRank=0
        em2=csv.reader(em1,delimiter=",")
        #em2.writerow([newVar,w])
        em3=csv.writer(em4)
        for rk in em2:
            if rk:
                #print("<h1>"+str(rk[0])+"</h1>")
                if rk[1]==w:
                    prevRank=int(str(rk[0]))
                    em3.writerow([newVar%151,])
                    #print("<h1>"+str(prevRank)+"</h1>")
                    break        
        if prevRank is newVar:
            sts="(no change)"
        elif prevRank > newVar:
            sts="(%d places up)"%(prevRank-newVar)
        else:
            sts="(%d places down)"%(newVar-prevRank)
        if prevRank is 0:
            sts="(new entry)"
    for i in ll:
        printVar+=str("<div class=\"rank\"><a href=\"%s\" target=\"rightone\"><h3>%d. "+w+"<br>%s</h3></a>""</div>")%(i[0],newVar,sts)
        break
    newVar+=1
printVar+="</div></body></html>"
#print("</body></html>")
print(printVar%("75%","8%","90%"))
