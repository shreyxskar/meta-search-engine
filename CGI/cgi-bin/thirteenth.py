import sys
import cgi
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

print("Content-type: text/html\r\n\r\n")



url="*****"
print("""
<html>
<head>
<title>Search results</title>

<style>
body
{
    background-color:white;
    
}
table.chk
{
border-radius:20px;
	background-color:black;
	color:white;
	border-collapse:separate;
	border-color:red;
	margin:10px 10px 10px 10px;
	padding:10px 10px 10px 10px;
	box-shadow: 5px 10px #888888;
	font-weight: bold;
	font-size:20px;	
}

div.outer_c
{
	background-color:black;
	border-radius:20px;
}

</style>

</head>
<body>""")
print("<center >")

def generateKey_Fk(inp):
    return inp.replace(' ','%20').lower()

ii,i=1,0

def generateData_Fk(url,fname):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")    
    tags = soup('div',attrs={"class":"_3wU53n"})
    t1=soup('div',attrs={"class":"_1vC4OE _2rQ-NK"})
    li=[]
    i=0    
    for tag,t2 in zip(tags,t1):
        i=i+1
        print("<tr><td>%s</td><td> %s</td></tr>"%(tag.contents[0],t2.contents[0].replace('₹','Rs ')))
        li.append([tag.contents[0],t2.contents[0].replace('₹','Rs ')])    
    myFile=open(fname,'a')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            wr.writerow(['Product Name','Price'])
            fl=1
        wr.writerows(li)
    return i

form=cgi.FieldStorage()
url1=form['urldataxxx'].value or "phones"
part1="https://www.flipkart.com/search?q="
FK=generateKey_Fk(url1)
part3="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
pgno=1
url=part1+FK+part3+str(pgno);
pgcount=int(form['totalpg'].value)
if pgcount >10:
    pgcount=10
fname=form['fname'].value+".csv"
print("<h3>Results in Flipkart for : %s(%d pages scraped)</h3><hr>"%(url1,pgcount))
print("<table class=\"chk\" border=2px>")
print("<th>Product Name</th><th>Price</th>")
for y in range(pgcount):
    linkdt=url[:url.rindex('=')+1]+str(pgno+y)
    i=i+generateData_Fk(linkdt,fname)
print("</table><br><hr>")
print("<h3>Results saved to <a src=\"X:\Abc\python\CGI\%s\">%s</a></h3>"%(fname,fname))
print("<h3 style=\"text-align:left\">%d items.</h3>"%i)
print("</center></body></html>")

