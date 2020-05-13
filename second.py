from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



url = input('Enter - ')
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
i=1
# Retrieve all of the anchor tags
tags = soup('a')#,attrs={"role":"row"})
print(soup.prettify())
for tag in tags:
    print(tag.contents[0])
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    i=i+1
    if i is 6:
        break
