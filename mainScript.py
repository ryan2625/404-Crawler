from bs4 import BeautifulSoup
from all_pages import arr
import requests
from openpyxl import Workbook
from creds import creds1
import time
from handleLogin import getSession

allSafeLinks = []
allBrokenLinks = []
miscBroken = []
linkCodeMatch = {}
arrTuple =[]
session = getSession()
n = 0

def handleNewLink(linkHref, link):
    if len(linkHref) > 3 and linkHref[:4] == "http" and linkHref != "https://":
        print(linkHref) 
        try: 
            code = session.get(linkHref, timeout=30)
        except Exception as e:
            linkCodeMatch[linkHref] = code
            allBrokenLinks.append(linkHref)
            arrTuple.append((link, linkHref, "ERR: TIMEOUT"))
            print("ERR", e)
            return
        code = str(code.status_code) 
    # Only mark link as safe if we get 200 level response
        if code[0] == "2": 
            allSafeLinks.append(linkHref)
        else:
            linkCodeMatch[linkHref] = code
            arrTuple.append((link, linkHref, code))
            allBrokenLinks.append(linkHref)

# If link is empty, href="javascript:void(0)"", #, etc
    else:
        miscBroken.append((link, linkHref))

def handleSubLinks(all_links, link):
    for subLink in all_links:
        linkHref = subLink['href'].strip()
        # Check if link doesn't include https (I.E href = "/myirem")
        if (len(linkHref) > 0) and linkHref[0] == "/":
            temp = linkHref
            linkHref = "https://www.irem.org" + temp
        
        # Linkedin and twitter don't like bots
        if len(linkHref) >=20 and (linkHref[:20] == "https://twitter.com/" or linkHref[:20] == "https://www.linkedin"):
            continue

        # If we already checked this link, no need to check again
        if (linkHref not in allSafeLinks and linkHref not in allBrokenLinks):
            handleNewLink(linkHref, link)
        
        else:
            if (linkHref in allBrokenLinks):
                code = linkCodeMatch[linkHref]
                arrTuple.append((link, linkHref, code))

def saveToExcel():
    wb = Workbook()
    ws = wb.active
    for tuples in arrTuple:
        ws.append([tuples[0], tuples[1], tuples[2]])
    wb.save("all_broken.xlsx")

    wb = Workbook()
    ws = wb.active
    for ele in miscBroken:
        ws.append([ele])
    wb.save("misc_broken.xlsx") 

    wb = Workbook()
    ws = wb.active 
    for ele in allSafeLinks:
        ws.append([ele])
    wb.save("all_safe.xlsx")

def main():
    session = getSession()
    for link in arr:
        n+=1 
        print("FILE", n)
        url = link
        tries = 0
        active = ""
        while active == "":
            if (tries >= 2) :
                break
            try: 
                active = session.get(url, timeout=10) 
            except:
                print("Main page timed out...")
                time.sleep(5)
                tries+=1
        if (tries >= 2) :
            allBrokenLinks.append(link)
            arrTuple.append((link, link, "ERR: MAIN TIMEOUT"))
            continue
        doc = BeautifulSoup(active.content, "html.parser")
        all_links = doc.find_all('a', href=True)
        handleSubLinks(all_links, link)
    saveToExcel()