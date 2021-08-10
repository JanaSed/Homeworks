import requests
from bs4 import BeautifulSoup as BS
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
r = requests.get(url, timeout=5, headers=headers)
soup = BS(r.content, 'html.parser')

contents = soup.find('table', class_="table table-compressed table-striped table-bordered")
# print(contents)

results = {}
for row in contents.find_all('tr'):
    row_data = row.find_all_next('td')
    # print(row_data)
    results[row_data[0].text] = [row_data[1].text, row_data[2].text, row_data[3].text, row_data[4].text, row_data[5].text, row_data[6].text, row_data[7].text, row_data[8].text, row_data[9].text]
    # print(results)

user_input = input('Please enter city name: ')
print(f'Õhutempiratuur: keskmine: {results[user_input][0]}; max: {results[user_input][1]}; min: {results[user_input][2]}\n'
      f'Maapinna min t: {results[user_input][3]}\n'
      f'Min t 2cm kõrgusel: {results[user_input][4]}\n'
      f'Suhteline õhuniiskus: keskmine: {results[user_input][5]}; min: {results[user_input][6]}\n'
      f'Tuule kiirus: keskmine: {results[user_input][7]}; max: {results[user_input][8]}\n'
      f'Sademed: {results[user_input][-2]}\n'
      f'Päikesepaiste kestus: {results[user_input][-1]}\n')
