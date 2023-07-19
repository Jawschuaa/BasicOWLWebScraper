from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.over.gg/players")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
alias = soup.findAll("div", attrs={"class": "alias"})
name = soup.findAll("div", attrs={"class": "name"})

for a, n in zip(alias,name):
    print(a.text + "-" + n.text)