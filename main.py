from bs4 import BeautifulSoup


#
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    pretty = doc.prettify()

title = doc.title
title.string = "HELP"
ptags = doc.find_all("p")[0]
print(doc.title.string)
print(doc.find_all("a"))
print(ptags.find_all("b"))