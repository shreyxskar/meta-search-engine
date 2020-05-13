import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Scrap:
    def __init__(self, query, fname, site, pgcount):
        self.query=query
        self.fname=fname
        self.site=site
        self.pgcount=pgcount        
        self.tags=[]
    def getUrl(self):
        if self.site is "fk":
            return query.replace(' ','%20').lower()
    def getBSTag(self):
        if self.site is 'fk':
            url = getUrl()
            html = urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            tags = soup('div',attrs={"class":"_3wU53n"})
            return tags
        xx=[]
        return xx;
    def scrapData(self):        
        ii,i=1,0
        tags = getBSTag()
        li=[]

        for tag in tags:
            i=i+1
            print(tag.contents[0])
            li.append([tag.contents[0]])

        myFile=open(fname,'a')
        fl=9
        with myFile:        
            wr=csv.writer(myFile)
            if fl is 9:
                wr.writerow(['Phone Model','Price'])
                fl=1
            wr.writerows(li)
        items=items+i
        print("%d items."%items)


q=input('Enter - ')
pg=1
fname=input("Filename - ")+".csv"


A1=Scrap(q, fname, 'fk', pg)
scrapData(A1)

print("Saved to %s file!"%A1.fname)

