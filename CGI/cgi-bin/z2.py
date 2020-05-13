import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import sqlite3
import cgi
import sys

print("Content-type: text/html\r\n\r\n")

printVar=""
#print("<h1>Hello</h1>")
printVar=printVar+'''
<html>
<head><title>z5</title>
<style>
button.abc
{

	text-align:center;
	transition:0.5s;
	width:%s;
	height:150px;
	text-decoration:bold;
	background-color:#FDAB9F;
	border:1px solid black;
	border-radius:10px;
	transition:0.7s;
	margin:5px 5px 5px 5px;
}
button.abc:hover
{
	text-align:center;
	height:180px;
	width:%s;
	font-size:20px;
	-webkit-text-stroke:0.5px white;
	
}
button:focus
{
	outline:none;
}


.pro:hover
{
    color:808080;
}
div.ctn
{
	
	background-color:C0C0C0;
	margin-bottom:10px;
	border-radius:7px;
	padding-left:10px;
	padding-right:10px;
}
</style>
</head>
<body>
<h3>%d search results in %d seconds.</h3>
<h3>Click on any result to proceed to checkout.</h3>
<br>
<center>
'''
#border: 7px solid #FFA500;


def myCr(qq,fname):
    ii,i=1,0
    shr=""
    url="https://www.croma.com/search/?text="+qq.replace(' ','+').lower()
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('h2')
    tags1 = soup('span',attrs={"class":"pdpPrice"})
    li=[]
    for tag ,tag1 in zip(tags,tags1):
        i=i+1
        ddb=fname+".db"
        conn=sqlite3.connect(ddb)
        stmt="insert into products values(\"%s\",\"%d\",\"%s\")"%(tag.contents[0],int(float(tag1.contents[0].replace('₹','').replace(',',''))),"Croma")
        conn.execute(stmt)
        conn.commit()
        #shr=shr+str(tag.contents[0])+" --> "+str(tag1.contents[0])+"\n"
        #print(tag.contents[0]," --> ",tag1.contents[0])
        li.append([tag.contents[0],tag1.contents[0].replace('₹',''),"Croma"])

    myFile=open(fname+".csv",'a')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            #wr.writerow(['Phone Model','Price'])
            fl=1
        wr.writerows(li)
    #print("%d items."%i)
    return shr


def myFk(qq,fname):
    shr=""
    ii,i=1,0
    url = "https://www.flipkart.com/search?q="+qq.replace(' ','%20').lower()+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('div',attrs={"class":"_3wU53n"})
    tags1 = soup('div',attrs={"class":"_1vC4OE _2rQ-NK"})
    li=[]
    for tag,tag1 in zip(tags,tags1):
            
        i=i+1
        ddb=fname+".db"
        conn=sqlite3.connect(ddb)
        stmt="insert into products values(\"%s\",\"%d\",\"%s\")"%(tag.contents[0],int(tag1.contents[0].replace('₹','').replace(',','')),"Flipkart")
        conn.execute(stmt)
        conn.commit()
        #shr=shr+str(tag.contents[0])+" --> "+str(tag1.contents[0])+"\n"
        #print(tag.contents[0]," --> ",tag1.contents[0])
        li.append([tag.contents[0],tag1.contents[0].replace('₹',''),"Flipkart"])

    myFile=open(fname+".csv",'w')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            wr.writerow(['Phone Model','Price','Website'])
            fl=1
        wr.writerows(li)
    #print("%d items."%i)
    return shr

def mySd(qq,fname):
    ii,i=1,0
    shr=""
    url="https://www.snapdeal.com/search?keyword="+qq.replace(' ','%20').lower()+"&santizedKeyword=samsung&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('p',attrs={"class":"product-title"})
    tags1 = soup('span',attrs={"class":"lfloat product-price"})
    li=[]
    for tag,tag1 in zip(tags,tags1):
        
        if qq in tag.contents[0].lower() or qq in "phones phone mobiles tvs tablets":
            i=i+1
            ddb=fname+".db"
            conn=sqlite3.connect(ddb)
            stmt="insert into products values(\"%s\",\"%d\",\"%s\")"%(tag.contents[0],int(tag1.contents[0].replace('Rs.  ','').replace(',','')),"Snapdeal")
            conn.execute(stmt)
            conn.commit()
            #shr=shr+str(tag.contents[0])+" --> "+str(tag1.contents[0])+"\n"
            #print(tag.contents[0]," --> ",tag1.contents[0])
            li.append([tag.contents[0],tag1.contents[0],"Snapdeal"])

    myFile=open(fname+".csv",'a')
    fl=9
    with myFile:        
        wr=csv.writer(myFile)
        if fl is 9:
            #wr.writerow(['Phone Model','Price'])
            fl=1
        wr.writerows(li)
    #print("%d items."%i)
    return shr
    #print(qq)



form=cgi.FieldStorage()


inp=form["query_bar"].value#input("Enter - ")
fname=form["fname_bar"].value#input("Filename - ")
pgs=form["optns"].value
srtg=form["sort"].value


for i in range(20000000):
    continue
#print("Results depend upon your internet speed!")
stttt=time.time()
shr=""

ddb=fname+".db"
conn=sqlite3.connect(ddb)

c=conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
if c.fetchone() is None:
    conn.execute('''CREATE TABLE if not exists products
                (name varchar(60),
                price int,
                website varchar(15));
                ''')
else:
    conn.execute("drop table products;")
    conn.execute('''CREATE TABLE if not exists products
                (name varchar(60),
                price int,
                website varchar(15));
                ''')


#shr=shr+"\n***********************FLIPKART*******************************\n"
#shr=shr+myFk(inp,fname)
#shr=shr+"\n*************************SNAPDEAL*****************************\n"
#shr=shr+mySd(inp,fname)
#shr=shr+"\n************************CROMA*********************************\n"
#shr=shr+myCr(inp,fname)
#print(shr)
#print("<h1>",srtg,"</h1>")

if pgs is "4":
    shr=shr+myFk(inp,fname)
    shr=shr+mySd(inp,fname)
    shr=shr+myCr(inp,fname)
elif pgs is "3":
    shr=shr+mySd(inp, fname)
elif pgs is "2":
    shr=shr+myFk(inp,fname)
else:
    shr=shr+myCr(inp,fname)



stmt="select * from products order by price %s"%str(srtg)

cursor=conn.execute(stmt)
i=1
for row in cursor:
    tpl=(i,row[0],int(row[1]),row[2])
    printVar=printVar+'''
            <a href="z14.py" class="xyz">
    <button class="abc">
    <h2 class="mdl">%d. %s</h2>
    <h2 class="prc">Rs. %d</h2>
    <h3 class="stqw">@%s</h3>
    </button>
    </a>
            '''%tpl
    i=i+1

    
printVar=printVar+''' </center>
    </body>
    </html>
'''
i=i-1
print(printVar%("50%","75%",i,time.time()-stttt))

#print("Total time taken : %d seconds"%(time.time()-st))

