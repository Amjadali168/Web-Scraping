import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# get the title of html page
title = soup.title
# print(title)

# get all the paragraph of the page
paras = soup.find_all('p') 
# print(paras)

# get all the anchor tag of the page
anchors = soup.find_all('a')
# print(anchors)

# get class of any element
print(soup.find('p')['class'])

# find all the element with class ""
print(soup.find_all("p", class_=""))

# get the text from the tag
print(soup.find('p').get_text())
print(soup.get_text())

# get all the anchor tag of the page
anchors = soup.find_all('a')
# print(anchors)

# get all the link on the page
for link in anchors:
    print(link.get('href'))