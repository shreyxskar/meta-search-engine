from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import csv


#fetch reviews for one hotel

tPages=1

'''
page 1: https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-or"+num+"-So_My_Resort-Calangute_North_Goa_District_Goa.html"
     2: https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-or5-So_My_Resort-Calangute_North_Goa_District_Goa.html#REVIEWS
     3: https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-or10-So_My_Resort-Calangute_North_Goa_District_Goa.html#REVIEWS
     4  https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-or15-So_My_Resort-Calangute_North_Goa_District_Goa.html#REVIEWS
page 6: https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-or25-So_My_Resort-Calangute_North_Goa_District_Goa.html#REVIEWS
'''
def fetchRev(n,str1):#="https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-or5-So_My_Resort-Calangute_North_Goa_District_Goa.html#REVIEWS"):
    lis=[]
    
    #str1
    for i in range(n):
        link=str1[:str1.rindex('-Reviews-')+len('-Reviews-')]+"or"+str(i*5)+str1[str1.rindex('-Reviews-')+len('-Reviews'):]
        #link=str1#[:str1.rindex('-or')+3]+str(i*5)+str1[str1.rindex('-or')+4:]
        lis.append(hotelReviews(link))
    return lis


def hotelReviews(link):
    html1=urlopen(link)
    sp=BeautifulSoup(html1,"html.parser")
    t4=sp.find_all('a',class_="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC")
    t5=sp.find_all('div',class_="social-member-event-MemberEventOnObjectBlock__event_type--3njyv")
    t3=sp.find_all('div',class_='ui_column is-12-tablet is-10-mobile hotelDescription')
    hnm=t3[0].h1.text
    revs=sp.find_all('q',class_="hotels-review-list-parts-ExpandableReview__reviewText--3oMkH")#,class_="hotels-review-list-parts-ExpandableReview__reviewText--3oMkH")
    li=[]
    newList=[]
    for rev,wtr,rdate in zip(revs,t4,t5):
        newList.append([hnm,link,wtr.text.encode('unicode-escape').decode('utf-8'),rdate.text[-6:].encode('unicode-escape').decode('utf-8').strip(),rev.text.encode('unicode-escape').decode('utf-8')])
    abc=open("reviews.csv","a")
    with abc:
        wr=csv.writer(abc)   
        wr.writerows(newList)
        

def onlyCall(str1):
    
    fetchRev(tPages,str1)
    



