import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import ssl
#import pandas as pd


url = input('Enter - ')or "https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
ii,i=1,0
tags = soup('div',attrs={"class":"_3wU53n"})
t1=soup('div',attrs={"class":"_1vC4OE _2rQ-NK"})
li=[]
#print(soup.prettify())
for tag,t2 in zip(tags,t1):# in t1:
    i=i+1
    #print(tag.contents[0]," --> ",t2.contents[0])
    li.append([tag.contents[0],t2.contents[0].replace('₹','Rs.')])
    
    #print(tag.contents[0])
#print(li)
myFile=open('ress.csv','w')
fl=9
with myFile:        
    wr=csv.writer(myFile)
    if fl is 9:
        wr.writerow(['Phone Model','Price'])
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
                print(row[0],"-->",row[1].replace('Rs.','₹'))
                
elif ch is not '0':
    print("Invalid choice!")
