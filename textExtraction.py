import os
try:
        from bs4 import BeautifulSoup
except:
        print("Error: BeautifulSoup (bs4) install required.")

extractData = open("FileReport/msft-10q_20190331.htm", "r", encoding="utf-8", errors = "ignore")

soup = BeautifulSoup(extractData, 'html.parser')
'''
for x in soup.find_all("p"):
    if(x.string == "MICROSOFT CORPORATION "):
        print(x.string)
'''

thisData = open("extractReport/extract.txt", "w+")
for x in soup.find_all('p'):
        if(str(x.string) == "None"):
                pass
        else:
                thisData.write(str(x.string))
                thisData.write("\n")
