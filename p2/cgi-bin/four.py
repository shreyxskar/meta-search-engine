import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

t3=soup.find_all('div',class_="social-member-event-MemberEventOnObjectBlock__event_type--3njyv")#,class_="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC")#,class_="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC")#class_='ui_column is-12-tablet is-10-mobile hotelDescription')

for i3 in t3:
    print(i3.text[-6:])
