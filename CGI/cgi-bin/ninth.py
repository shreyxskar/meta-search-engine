import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')or "https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

'''pix=soup.div.img['src']
pli=[]
i=0
for pi in pix:
    i=i+1
    pli.append(pi.get('src'))
    #if i is 24:
    #    break

print(pli)
#print(pli[0])
#print(pli[len(pli)-1])
print("Length of each",pli.count('<'))
print(i," items.")


'''
li=[]
for i in soup.find_all('div'):
    if i.img:
        li.append(i.img)
print(li)
print(len(li))
