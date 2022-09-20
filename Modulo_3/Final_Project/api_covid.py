import requests
import datetime as dt
import csv
from PIL import Image
from IPython.display import display
from urllib.parse import quote

url = 'https://api.covid19api.com/dayone/country/brazil'
request = requests.get(url)

raw_data = request.json()

final_data = []
for obs in raw_data:
    final_data.append([
        obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'],
        obs['Date']
    ])

final_data.insert(0, ['Confirmed', 'Deaths', 'Recovered', 'Active', 'Date'])

confirmed = 0
deaths = 1
recovered = 2
active = 3
date = 4

for element in range(1, len(final_data)):
  final_data[element][date] = final_data[element][date][:10]

with open('Modulo_3/Final_Project/brasil-covid.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(final_data)

for element in range(1, len(final_data)):
  final_data[element][date] = dt.datetime.strptime(final_data[element][date], '%Y-%m-%d')

def get_datasets(y, labels):
  if type(y[0]) == list:
    datasets = []
    for element in range(len(y)):
      datasets.append({
        'label': labels[element],
        'data': y[element]
      })
    return datasets
  else:
    return [{
      'label': labels[0],
      'data': y
    }]

def set_title(title=''):
  if title != '':
    display = 'true'
  else:
    display = 'false'
  return{
    'title': title,
    'display': display
  }

def create_chart(x, y, labels, kind='bar', title=''):
  datasets = get_datasets(y, labels)
  options = set_title(title)

  chart = {
    'type': kind,
    'data': {
      'labels': x,
      'datasets': datasets
    },
     'options': options 
  }
  return chart

def get_api_chart(chart):
  url_base = 'https://quickchart.io/chart'
  req = requests.get(f'{url_base}?c={str(chart)}')
  return req.content

def get_api_qrcode(link):
  text = quote(link)
  url_base = 'https://quickchart.io/qr'
  req = requests.get(f'{url_base}?text={text}')
  return req.content

def save_image(path, content):
  with open(path, 'wb') as image:
    image.write(content)

def display_image(path):
  img_pil = Image.open(path)
  display(img_pil)

y_data_1 =[]
for obs in final_data[1::10]:
  y_data_1.append(obs[confirmed])

y_data_2 =[]
for obs in final_data[1::10]:
  y_data_2.append(obs[recovered])

y_data_3 =[]
for obs in final_data[1::10]:
  y_data_3.append(obs[active])


labels = ['Confirmed', 'Recovered', 'Active']
x = []

for obs in final_data[1::10]:
  x.append(obs[date].strftime('%Y/%m/%d'))

chart = create_chart(x, [y_data_1, y_data_2, y_data_3], labels, title ='Confirmed vs Recovered vs Active')
chart_content = get_api_chart(chart)
save_image('Modulo_3/Final_Project/img/my_first_graph_covid.png', chart_content)
display_image('Modulo_3/Final_Project/img/my_first_graph_covid.png')

url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('Modulo_3/Final_Project/img/qrcode.png', get_api_qrcode(link))
display_image('Modulo_3/Final_Project/img/qrcode.png')
