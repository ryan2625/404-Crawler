from bs4 import BeautifulSoup
import requests

url = "https://www.irem.org/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

content = doc.find_all(text="IREM")

var = content[0].parent

print(var.find("span"))