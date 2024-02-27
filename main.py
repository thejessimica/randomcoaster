import requests
from bs4 import BeautifulSoup
import lxml
import html5lib

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3"
}

item_name = "Snow Dragon Stuffed Animal"
web_link = "https://rcdb.com/"
response = requests.get(web_link, headers=HEADERS)

web_page = response.text

soup = BeautifulSoup(web_page, "html5lib")

coaster_name = soup.select("#rrc_text > p:nth-child(2) > a")
coaster_park = soup.select("#rrc_text > p:nth-child(3) > a")
coaster_location = soup.select("#rrc_text > p:nth-child(4)")

data = []

if coaster_name:
    print(coaster_name[0].text)
    data.append(coaster_name[0].text)
else:
    print("Name not found")

if coaster_park:
    print(coaster_park[0].text)
    data.append(coaster_park[0].text)
else:
    print("Park not found")

if coaster_location:
    print(coaster_location[0].text.replace("Location", "").strip())
    data.append(coaster_location[0].text.replace("Location", "").strip())
else:
    print("Location not found")


print(data)
