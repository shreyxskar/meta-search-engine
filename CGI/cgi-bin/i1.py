from bs4 import BeautifulSoup
from urllib.request import urlopen

url = input('Enter - ')or "https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
ii,i=1,0
#tags = soup('div')#,attrs={"class":"_3wU53n"})
m_con=soup.find_all('div',class_="lister-item mode-advanced")

#print(type(m_con)) '''<class 'bs4.element.ResultSet'>'''

li=[]
#print(soup.prettify())
   
for tag in m_con:# in t1:
    i=i+1
    print(tag.h3.find('span',class_="lister-item-year text-muted unbold").text)
    #print(len(tag.h3))
    
print("Done",i)
print(len(m_con))
