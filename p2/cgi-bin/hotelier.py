import os.path
import sqlite3
import cgi

print("Content-type: text/html\r\n\r\n")

baseDir=os.path.dirname(os.path.abspath(__file__))
db=os.path.join(baseDir,"tripAdvisor.db")

conn=sqlite3.connect(db)
form=cgi.FieldStorage()
inp=form.getvalue('inph_bar') or " "
#inp=input("Enter keyword : ")
ss=[]
printVar="""<html>
<head><title>Hotel list for reviews</title></head><style>
div.hn
{
text-align:center;
padding: 10px 10px 10px 10px;
    padding: 10px 10px 10px 10px;
    width:%s;
    color:white;
    
    background-color:#00A680;
    border-radius:10px;
    transition:0.4s;
}
div.hn:hover
{
    width:%s;
    color:black;
}
fieldset
{
    width:%s;
    text-align:left;
    border:3px dotted black;
}

</style><body><h1>%s hotels found '%s' :</h1><center>"""
newDict={}
ss.append("%"+inp.replace(' ','%')+"%")
#ss=["%worst%","%bad%experience%","%bad%food%","%bad%room%","%major issue%"]
for k in ss:
    stmt="SELECT distinct * FROM HOT_REV WHERE review like \""+k+"\";"
    res=conn.execute(stmt)
    #print(stmt)
    j=0
    #print("Hotels List")  .replace('%','percent')
    for i in res:
        if i[0] in newDict:
            newDict[i[0]]+="<fieldset><legend><h4>"+i[2].replace('%','percent')+" on "+i[3].replace('%','percent')+"</h4></legend>"+i[4].replace('\\u2026','!').replace('%','percent')+"</fieldset>"
        else:
            newDict[i[0]]="<fieldset><legend><h4>"+i[2].replace('%','percent')+" on "+i[3].replace('%','percent')+"</h4></legend>"+i[4].replace('\\u2026','!').replace('%','percent')+"</fieldset>"
        


        #print(i[0])
        #print("Hotel Name :",i[0],"\nReview by :",i[1],"\nDate :",i[2],"\n",i[3],sep="")
       
        j+=1
    #print(j,"reviews")#,k)
#print(newDict)
#printVar+=""
for i in newDict:
    printVar+="<div class=\"hn\"><h2>"+i+"</h2><center>"
    printVar+=newDict[i]+"</center></div><br><br>"
    #print(newDict[i])
    #print()
#print(len(newDict))
#printVar+=str(j)+" reviews</body></html>"
printVar+="</center></body></html>"
print(printVar%("75%","90%","60%",str(len(newDict)),inp))
