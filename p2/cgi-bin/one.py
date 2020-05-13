from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import csv
import three

#fetches URLs of Goa Hotels(for reviews)


'''page 1: https://www.tripadvisor.in/Hotels-g297604-Goa-Hotels.html
   page 2: https://www.tripadvisor.in/Hotels-g297604-oa30-Goa-Hotels.html
           https://www.tripadvisor.in/Hotels-g297604-oa60-Goa-Hotels.html
           https://www.tripadvisor.in/Hotels-g297604-oa90-Goa-Hotels.html
           https://www.tripadvisor.in/Hotels-g297604-oa120-Goa-Hotels.html
       136 https://www.tripadvisor.in/Hotels-g297604-oa4050-Goa-Hotels.html
'''


def myURL(i):
    url="https://www.tripadvisor.in/Hotels-g297604-oa"+str(i)+"0-Goa-Hotels.html"
    #url=input("Enter URL : ")
    return url


def hotelNames(i):
    url=myURL(i)
    html=urlopen(url)
    soup=BeautifulSoup(html,"html.parser")
    hotel=[]
    t1=soup.find_all('div',class_="ui_column is-8 main_col allowEllipsis ")#"media-image-ResponsiveImage__default--1s-9x")#,class_="prw_rup prw_meta_hsx_responsive_listing ui_section listItem")    
    for i1 in t1:
        hotel.append(i1.a['href'])
        #print(i1.a.text)
        #print()
    #print(len(t1),"items")
    #print("Done")
    return hotel


def perPage(n):
    hotels=[]
    for i in range(n):
        hotels.append(hotelNames(i))
    return hotels
    #hotelNames(i)


def hotelReviews(hotel_links):
    sz=len(hotel_links)
    lll=[]
    for ht in hotel_links:
        qq=time.time()
        rURL="https://www.tripadvisor.in"+ht
        lll.append(rURL)            
        three.onlyCall(rURL)
        print("Start time ->",qq,"End time ->",time.time())
    fi=open("hotel_list.csv","w")
    with fi:
        cw=csv.writer(fi)
        cw.writerow(lll)
        #print(rURL)
   # print(sz)

    

        

totalPages=10
s_time=time.time()
hotels=perPage(totalPages)
#print(hotels)
mFile=open("reviews.csv","a")
with mFile:
    wr=csv.writer(mFile)
    wr.writerow(['Hotel Name','Hotel Review Page','Guest Name','Review Date','Hotel Review'])
for x in range(totalPages):    
    hotelReviews(hotels[x])
print(len(hotels))
#print(hotels)
print("%d seconds."%(time.time()-s_time))


