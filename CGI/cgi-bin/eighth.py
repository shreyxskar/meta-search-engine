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
<title>2</title>
</head>
<body>""")
print("<center >")#<div style=\"padding:15px;border:2px solid black;width:80%;height:100%\">")

#print("<h3>Your link is <br><a style=\"color:red\" href=\"",url,"\">",url,"</a></h3><br>")



def generateKey_Fk(inp):
    return inp.replace(' ','%20').lower()

def generateKey_Am(inp):
    return inp.replace(' ','+').lower()


ii,i=1,0
def generateData_Fk(url,fname):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")    
    tags = soup('div',attrs={"class":"_3wU53n"})
    t1=soup('div',attrs={"class":"_1vC4OE _2rQ-NK"})
    li=[]
    i=0
    #print("<table class=\"chk\" border=2px>")
    for tag,t2 in zip(tags,t1):
        i=i+1
        print("<tr><td>%s</td><td> %s</td></tr>"%(tag.contents[0],t2.contents[0].replace('₹','Rs ')))
        li.append([tag.contents[0],t2.contents[0].replace('₹','Rs ')])
    
    
    #print("</table>")
    myFile=open(fname,'a')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            wr.writerow(['Product Name','Price'])
            fl=1
        wr.writerows(li)
    return i




#amazon
'''
def generateData_Am(url,fname):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")    
    tags = soup('span',attrs={"class":"a-size-medium a-color-base a-text-normal"})
    t1=soup('span',attrs={"class":"a-price-whole"})
    li=[]
    i=0
    #print("<table class=\"chk\" border=2px>")
    for tag,t2 in zip(tags,t1):
        i=i+1
        print("<tr><td>%s</td><td> %s</td></tr>"%(tag.contents[0],t2.contents[0].replace('₹','Rs ')))
        li.append([tag.contents[0],t2.contents[0].replace('₹','Rs ')])
    
    
    #print("</table>")
    myFile=open(fname,'a')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            wr.writerow(['Product Name','Price'])
            fl=1
        wr.writerows(li)
    return i


    


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

form=cgi.FieldStorage()
url1=form['urldataxxx'].value or "phones"#"https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"





#inp=input("Enter search string -> ")
part1="https://www.flipkart.com/search?q="
FK=generateKey_Fk(url1)
part3="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
pgno=1

url=part1+FK+part3+str(pgno);
'''
newV=generateKey_Am(url1)
url2="https://www.amazon.in/s?k="+newV+"&page="+str(pgno)




print("""
<html>
<head>
<title>2</title>
</head>
<body>""")
print("<center >")

print("<h3>Your link is <br><a style=\"color:red\" href=\"",url,"\">",url,"</a></h3><br>")


'''
#<div style=\"padding:15px;border:2px solid black;width:80%;height:100%\">")

#umake=""

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
'''
print("<h3>Results in Amazon for : %s(%d pages scraped):</h3><hr>"%(url1,pgcount))

print("<table class=\"chk\" border=2px>")
print("<th>Product Name</th><th>Price</th>")
for y in range(pgcount):
    linkdt=url2[:url2.rindex('=')+1]+str(pgno+y)
    i=i+generateData_Am(linkdt,fname)

print("</table>")
'''
#print(url)

'''

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
ii,i=1,0
tags = soup('div',attrs={"class":"_3wU53n"})
t1=soup('div',attrs={"class":"_1vC4OE _2rQ-NK"})
#pix=soup('img',attrs={"class":"_1Nyybr  _30XEf0"})
li=[]
#print(soup.prettify())

print("<table class=\"chk\" border=2px>")
for tag,t2 in zip(tags,t1):# in t1:
    i=i+1
    print("<tr><td>%d</td><td>%s</td><td> %s</td></tr>"%(i,tag.contents[0],t2.contents[0].replace('₹','Rs ')))
    li.append([tag.contents[0],t2.contents[0].replace('₹','Rs ')])
    
    #print(tag.contents[0])
#print(li)
print("</table>")
myFile=open('reslist.csv','w')
fl=9
with myFile:        
    wr=csv.writer(myFile)
    if fl is 9:
        wr.writerow(['Product Name','Price'])
        fl=1
    wr.writerows(li)


    '''
print("<h3>Results saved to %s</h3>"%fname)
print("<h3 style=\"text-align:left\">%d items.</h3>"%i)
print("</center></body></html>")
#print("End")
