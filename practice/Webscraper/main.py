from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

for title in soup.find_all(class_="titlelink"):
    print(title.string)