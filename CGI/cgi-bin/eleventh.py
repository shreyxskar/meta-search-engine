import sys
import cgi
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


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
        print(tag.contents[0],t2.contents[0].replace('₹','Rs '))
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

url=input("Enter -> ")
fname="testing.csv"
print(generateData_Am(url,fname))
