from bs4 import BeautifulSoup
from lxml import etree

import re
import requests
import json
import io
import os
import sys
import time

res = requests.get('https://shimo.im/docs/PPCHcQthvqp3qpkP')
print(res.text)
htmlData = res.text

soup = BeautifulSoup(htmlData)
trs=soup.findAll("p")
length=len(trs)
print(trs)

data = {
   'notices': []
}

for index in range(len(trs)):
   print(trs[index])
   code = str(trs[index])
   rc = re.compile("\<.*?\>" )
   new = rc.sub('',code)
   data['notices'].append(new)
         
fp = open("notices.json", "w")
strToJson = json.dump(data, fp)
print(strToJson)

logFd = open("lastUpdate", "w")
logFd.write(str(time.time()))


