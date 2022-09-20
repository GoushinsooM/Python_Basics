import csv

header = ['nome', 'sobrenome']
data = []
opt = input('O que deseja fazer?\n 1-Cadastrar \n 0-Sair \n')

while opt != '0':
  name = input('Qual é o seu nome? ')
  surname = input('Qual é seu sobrenome? ')
  data.append([name, surname])
  opt = input('O que deseja fazer?\n 1-Cadastrar \n 0-Sair')

with open('src/users.csv', 'w') as file_csv:
  writer = csv.writer(file_csv)
  writer.writerow(header)
  writer.writerows(data)

with open('src/users.csv', 'r') as csv_file:
  reader = csv.reader(csv_file, delimiter=',')
  for row in reader:
    print(row)