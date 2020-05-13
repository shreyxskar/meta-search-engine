import sys
import cgi
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

print("Content-type: text/html\r\n\r\n")

print("""
<html>
<head>
<title>1</title>
</head>
<body>
<center style="padding-top:15px">
<div class="outer_c" name="oc" style="border:2px solid black;width:700px;">
<h1>Data Scraping</h1><hr><br><br>
<h3>Contents found </h3>
<br><br>""")

f1=cgi.FieldStorage()
url=f1["urldata"].value
try:
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    ii=1
    i=0
    tags = soup('div',attrs={"class":"_3wU53n"})
    t1=soup('div',attrs={"class":"_1vC4OE _2rQ-NK"})
    li=[]
    for tag,t2 in zip(tags,t1):
        i=i+1
        li.append([tag.contents[0],t2.contents[0].replace('₹','Rs.')])    
    myFile=open('ress.csv','w')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            wr.writerow(['Phone Model','Price'])
            fl=1
        wr.writerows(li)
    print("<table style=\"border:2px solid black\">")
    with open('ress.csv') as fi:
        rd=csv.reader(fi,delimiter=',')
        for row in rd:
            print("<tr>")
            if row:
                if ii is 1:
                    ii=2
                    continue
                print("<td>%s</td><td>%s</td></tr>"%(row[0],row[1].replace('Rs.','₹')))
    print("</table>")
except:
    raise

print("""</div></center></body></html>""")
