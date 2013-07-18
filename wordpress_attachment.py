#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup
#Variables to modify
URL="http://localhost/wordpress/"
start_count=0
end_count=1000
#don't modify below this
for n in range(start_count,end_count):
  exp_url=URL+"?attachment_id=" + str(n)
  r=requests.get(exp_url,allow_redirects=False)
  if 200 == r.status_code:
    soup=BeautifulSoup(r.text)
    #image
    each_div=soup.find('div',{'class':'attachment'})
    if each_div != None:
      tar_img=each_div.find('a').find('img')['src']
      tar_link=each_div.find('a')['href']
      if tar_img == "":
        print str(n) + " : " + tar_link
      else:
        print str(n) + " : " + tar_img
      tar_img=""
    else:
    #all others (tested with pdf,html and some more)
      each_div=soup.find('p',{'class':'attachment'})
      print str(n) + " : " + each_div.find('a')['href']
