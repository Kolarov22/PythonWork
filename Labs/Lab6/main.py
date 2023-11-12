import requests
from bs4 import BeautifulSoup
import re

req = requests.get("http://books.toscrape.com/")
cont = req.content
soup = BeautifulSoup(cont, "html.parser")
header = soup.find("header").text
#print(header)

pager = soup.find("li", attrs={"class":"current"}).text
#print(pager)

button = soup.find("button").text
# print(button)

product = soup.findAll("article", attrs={"class":"product_pod"})


title_pattern = re.compile(r'<a[^>]*\stitle="([^"]*)"')
title = title_pattern.findall(str(product))

price_pattern = re.compile(r'<p\s+class="price_color">([^<]+)</p>')
price = price_pattern.findall(str(product))

# print(title)
# print(price)

books = soup.find("ul", attrs={"class":"nav"})
if books:
    litags = books.findAll("li")

    for litag in litags:
        atag = litag.find("a")
        if atag:
            text = atag.get_text(strip=True)
            print(text)

imgs = soup.findAll("img")
alt_pattern = re.compile(r'<img\s+[^>]*alt="([^"]+)"')
alt= alt_pattern.findall(str(imgs))
#print(alt)










