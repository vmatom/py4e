import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('p')
count_par = 0
for tag in tags:
    count_par += 1
# https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html - Easy scrapping
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/ - Hard scrapping
print ( "paragraphs in this url are - ", count_par)
