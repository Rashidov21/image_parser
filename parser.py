import time
import requests
import wget 
from bs4 import BeautifulSoup

url = "https://sibmama.ru/objavlenie-01-04.htm"

HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

page = requests.get(url=url, headers=HEADERS)

print(page.status_code) # 200

soup = BeautifulSoup(page.text, "html.parser")

strong_tags = soup.find_all("strong")
for element in strong_tags:
    if element.find("img"):
        img = element.find("img")
        download_url = "https://sibmama.ru" + img.get("src")
        wget.download(url=download_url, out="images/")
        print("Dowloaded !")
        time.sleep(1)