from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
s,i=0,0
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    if i>5:
        break
    else:
        print(tag.contents[0]);
        i=i+1
#print("Sum : ",s);


    
    # Look at the parts of a tag
   # print('TAG:', tag)
    #print('URL:', tag.get('href', None))
  #  print('Contents:', tag.contents[0])
   # print('Attrs:', tag.attrs)
