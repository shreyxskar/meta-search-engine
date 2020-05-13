from bs4 import BeautifulSoup
from urllib.request import urlopen

url=input("Enter -> ")
html=urlopen(url)
soup=BeautifulSoup(html,"html.parser")

t1=soup.find_all('div')#,class_="s-item-container")

for i1 in t1:
    print(i1.div)
print("%d items."%len(t1))

print("Done")
