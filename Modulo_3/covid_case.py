import requests
import datetime

url = 'https://api.covid19api.com/country/brazil'
request = requests.get(url)

covid_list = request.json()

for case in covid_list:
  if case.get('Confirmed') == 1:
    first_case = case.get('Confirmed')
    date = case.get('Date')
    country = case.get('Country')
    print(f'Foi confirmado o {first_case} caso de covid no {country} em {date[:10]}')
    break
  else:
    pass
