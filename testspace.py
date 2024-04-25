from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/IREM_info"
result = requests.get(url)
doc = BeautifulSoup(result.content, "html.parser")
print(doc)

links = doc.find_all('a', href="https://twitter.com/IREM_info")
test = requests.get("https://twitter.com/IREM_info")
print(test.status_code)
