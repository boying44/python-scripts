import sys
from bs4 import BeautifulSoup
import requests
import mechanize

r = requests.get("http://" + "www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/")
data = r.text
soup = BeautifulSoup(data, 'html.parser')

links = soup.find_all('a')
# for link in links:
#    print(link.get('href'))

link = links[10].get('href')
br = mechanize.Browser()
br.set_handle_robots(False)
# response = br.open(link)
response = br.open("https://amazon.com")

print link
print response.read()
# response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
