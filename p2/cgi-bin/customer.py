import sqlite3
import cgi
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "tripAdvisor.db")
print("Content-type: text/html\r\n\r\n")
conn=sqlite3.connect(db_path)
form=cgi.FieldStorage()
inp=form.getvalue("inp_bar") or " "

printVar="""
<html><head>
<title>List of Hotels in Goa</title>
<style>
body{font-family:lucida console;}

div.hotelname
{
    width:%s;
    color:white;
    height:55px;
    background-color:#00A680;
    border:0.1px solid #00A680;
    border-radius:3px;
    font-size:20px;
    
    transition:0.4s;
}
div.hotelname:hover
{
    width:%s;
    font-size:25px;
    color:black;
}
a
{
transition:0.5s;
    color:black;
    text-decoration:none;
}
a:hover
{color:white;}

</style></head>
<body><h2>%d hotels found.</h2>
<div name="list_h">
"""
#<iframe name="browser1" width="60%" height="70%"></iframe>

#inp=input("Enter keyword : ")
ss=[]#["%great%"]
ss.append("%"+inp.replace(' ','%')+"%")

#ss=["%worst%","%bad%experience%","%bad%food%","%bad%room%","%major issue%"]
for k in ss:
    stmt="SELECT distinct HOTEL_NAME,HOTEL_LINK FROM HOT_REV WHERE review like \""+k+"\" order by REVIEW;"
    res=conn.execute(stmt)
    #print(stmt)
    j=0
    #print("Hotels List")
    for i in res:
        #print(i[0])
        printVar+="""<h2><a href="%s" target="browser1"><div class="hotelname"><center>%s</a></center></h2></div>"""%(i[1],i[0])
        #print()
        j+=1
    #print(j,"reviews")
    #print()#,k)
wd,hg="60%","70%"

printVar+="""</div></body></html>"""
print(printVar%("75%","100%",j))#,wd,hg))
