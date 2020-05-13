import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import ssl
#import pandas as pd

#print("Content-type: text/html\r\n\r\n")
#url = input('Enter - ')or "https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
url="https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
ii,i=1,0
tags = soup("div",attrs={"class":"hGSR34"})

li=[]
#s=soup.prettify()
#print(s)
#print(tags.prettify())
for tag in tags:# in t1:
    i=i+1
    #print(tag.contents[0]," --> ",t2.contents[0])
    if tag is not None:
        li.append([tag.contents[0]])
        print(tag.contents[0])
        print("")
print(i,"items.")
print(li)
#print(li)
'''
myFile=open('ress.csv','w')
fl=9
with myFile:        
    wr=csv.writer(myFile)
    if fl is 9:
        wr.writerow(['Phone Model'])
        fl=1
    wr.writerows(li)
print("Saved to .csv file!")
print("%d items."%i)
ch=input("To view details enter '1' else '0' : ")
if ch is '1':
    with open('ress.csv') as fi:
        rd=csv.reader(fi,delimiter=',')
        for row in rd:
            if row:
                if ii is 1:
                    ii=2
                    continue
                print(row[0])
                
elif ch is not '0':
    print("Invalid choice!")'''
