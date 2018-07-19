import sys
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import requests

full_data = []
pos  = []  
pos1=[]

file = open('/home/vinoth/www.allitebooks.com/downloads/21stcent/index.html.114')
content = file.read()
soup1 = BeautifulSoup(content,'html.parser') # choose lxml parser
soup2 = soup1.find('div', {'class':"entry-body-thumbnail hover-thumb"})
image_tags = soup2.findAll('img')
for eleme in image_tags:
	pos.append(eleme.get('src'))
	print(pos[0])

dl_data = soup1.find_all("dt")
dl_data1 = soup1.find_all("dd")

x=0
str1 = []
for dlitem in dl_data:
	str1.append(dlitem.string) 
	x=x+1
print(str1)

str2 = [] 
for dditem in dl_data1:
	str2 = dditem.text	
print(str2)

css_soup = soup1.find('div',{'class':"entry-content"})
print(css_soup.find('h3').text)
print(css_soup.find('p').text)

soup3 = soup1.find('span', {'class':"download-links"})
download_tags = soup3.findAll('a')
for element in download_tags:
	pos1.append(element.get('href'))
	print(pos1[0])
			
comp_info = pd.DataFrame()
info = soup1.find('div',{'class':"book-detail"}).extract()
table =info.findAll('div')
for element in table:
	pos1.append(element.get('dt'))
	print(pos1)
answer = [] 
heading=[]
for i in info.find_all('dt'):
	heading.append(i.text)
for i in info.find_all('dd'):
	answer.append(i.text)

comp_info['Id of book'] = heading
comp_info['Attribute of book ']  = answer
print(comp_info)


