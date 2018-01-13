url = "https://osu.ppy.sh/p/packlist?t=r"
login= "https://osu.ppy.sh/forum/ucp.php?mode=login"
uname = ""
pword = ""

import sys
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# login
payload = {
	"username": uname, 
	"password": pword
}

session_requests = requests.session()
res = session_requests.post(
	login, 
	data = payload,
)
print res.content
# login

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

links = soup.find_all('a')
for link in links:
   r = requests.get(link.get('href')))

