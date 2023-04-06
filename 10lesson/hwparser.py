from bs4 import BeautifulSoup
import requests

url = 'https://ru.wikipedia.org/wiki/Loathe'
all_text = []
res_text = []
res_text1=[]
res_text2=[]
search_response = requests.get(url)
print(search_response)
soup=BeautifulSoup(search_response.text, 'html.parser')
#print(soup)
all_text = soup.find_all('p')
#print(all_text)
all_text_1 = soup.find_all('dt')
all_text_2 = soup.find_all('li')
#print(all_text_1)
#print(all_text_2)
for data in all_text:
    res_text.append(data.text)

for data in all_text_2:
    res_text2.append(data.text)

for data in all_text_1:
    res_text1.append(data.text)
#print(res_text)
for data in res_text:
    print(data)
print(res_text1)
for data in res_text2[6:15]:
    print(data)
