import requests
from bs4 import BeautifulSoup
from selenium import webdriver

r1 = requests.get(punchng.com)
r1.status_code

coverpage = r1.content  #coverpage content
soup_one = BeautifulSoup(coverpage,'html5lib')
coverpage_news = soup_one.find_all('h2', class_='Top News')  #identify news
coverpage_news[4].get_text()  #extract text
coverpage_news[4]['href']      #access the link

