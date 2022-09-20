sus = 0
question_1 = input('Mora perto da vítima? ').lower()
question_2 = input('Já trabalhou com a vítima? ').lower()
question_3 = input('Telefonou para a vítima? ').lower()
question_4 = input('Esteve no local do crime? ').lower()
question_5 = input('Devia para a vítima? ').lower()

if question_1 == 'sim':
  sus += 1
if question_2 == 'sim':
  sus += 1
if question_3 == 'sim':
  sus += 1
if question_4 == 'sim':
  sus += 1
if question_5 == 'sim':
  sus += 1

if sus == 5:
  print('Você é o assassino!')
elif sus >= 3:
  print('Você é cumplice!')
elif sus == 2:
  print('Você é suspeito...')
else:
  print('liberado')