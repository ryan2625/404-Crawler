from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from creds import creds1
import time
from all_pages import arr
from pprint import pprint

'''
url = "https://www.irem.org/chapters/canadian-chapter-resources/chapter-services-for-canada"

page = requests.get(url)

page = BeautifulSoup(page.content, "html.parser")

print(page.prettify())

for link in arr:
    code = requests.get(link)
    print(str(code.status_code))
    '''


url = "https://www.irem.org/sso/login.aspx"

res = requests.get()


'''
https://www.irem.org/sso/login.aspx
Make post request with EMAIL
get(url) LOCATION

THEN
make post request with username and password

https://my2.irem.org/SSO/LoginTemplates/DefaultLogin.aspx?vi=8&vt=36df599efebfc7e19146a16b1d829de21fe447922d3a8bf0415de476cb65c83ae288a95a7436848396e812fce24686f46e527b897502630b58f2c4c317acc61c
'''