from bs4 import BeautifulSoup
import requests

list = []
dud = []
url = "https://www.irem.org/"

result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")


links = doc.find_all('a', href=True)

# Extract and print the URLs
for link in links:
    temp = link['href']
    if (len(temp) > 0) and temp[0] == "/":
        link2 = "https://www.irem.org" + temp
        temp = link2

    if temp[:4] == "http":
        test = requests.get(temp)
        test = str(test.status_code) 
        if test[0] == "4": 
            list.append(temp)
    else:
        dud.append(temp)

    print(temp)

print(list)