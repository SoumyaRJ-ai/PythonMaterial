"""
Purpose: scraping
"""
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.whoishostingthis.com/tools/user-agent/", timeout=60)
soup = BeautifulSoup(res.text, "lxml")
print(soup.prettify())
