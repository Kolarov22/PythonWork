import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://www.scrapethissite.com/pages/simple/")
cont = req.content
page = BeautifulSoup(cont, "html.parser")
country = page.findAll(attrs={"class" : "country"})
info = []
for c in country:
    name = c.find("h3").get_text(strip=True)
    capital = c.find(attrs={"class" : "country-capital"}).get_text(strip=True)
    population = c.find(attrs={"class" : "country-population"}).get_text(strip=True)
    area = c.find(attrs={"class" : "country-area"}).get_text(strip=True)
    info.append([name, capital, population, area])
df = pd.DataFrame(data = info)
df.columns = ["Country", "Capital", "Population", "Area"]
df.to_excel("countries.xlsx")



# nav = page.find(attrs={"class" : "nav"})
# if nav:
#     lis = nav.findAll("li")
#     for li in lis:
#         a = li.find("a")
#         print(a["href"])

# footer = page.find(attrs={"id" : "footer"}).get_text(strip=True)
# print(footer)

# sect = page.find(attrs={"class" : "col-md-6"})
# parent = sect.findParent()
# print(parent)




