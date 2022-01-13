from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://webscraper.io/test-sites/tables"
page = requests.get(url).content

soup = BeautifulSoup(page, "html.parser")

tables = soup.find_all('table')
table = soup.find('table', class_='table-bordered')
dataframe = pd.DataFrame(columns=['First Name', 'Last Name', 'Username'])

for tr in table.find_all('tr'):
    td = tr.find_all('td')

    if td:
        id = td[0].text
        first_name = td[1].text
        last_name = td[2].text
        username = td[3].text

        dataframe = dataframe.append({'First Name': first_name,
                                      'Last Name': last_name,
                                      'Username': username},
                                     ignore_index=True)

print(dataframe.head())