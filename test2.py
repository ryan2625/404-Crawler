from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

arr = [
    "https://www.irem.org/CommonLogin/login?ReturnUrl=%2Fadmin%2Fdefault.aspx",
    "http://127.0.0.1:5500/regex-repo-searcher/src/index.html",
    "https://github.com/ryan2625",
    "https://nmhc%20%7c%2c%20%7c%20new%20research%20fin%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20r%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20rds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%c%20%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%c%20%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%c%20%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%c%20%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%c%20%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%c%20%7c%20new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%0new%20research%20finds%20rent%20control%20and%20other%20rent%20regulation%20laws%20hurt%20renters%20seeking%20housing%20opportunity%20and%20affordability,%20and%20disproportionally%20benefit%20higher%20income%20renters",
    "https://github.com/ryan2625",
    "http://127.0.0.1:5500/regex-repo-searcher/src/iasdasdndex.html"
]


for link in arr:
    try :
        requests.get(link)
    except Exception as e:
        print(e)


print("All done!")