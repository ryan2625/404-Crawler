from bs4 import BeautifulSoup
import requests

url = "https://www.irem.org/"

result = requests.get(url)

print(result.text)