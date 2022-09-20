age = int(input('Idade: '))
salary = float(input('Salário: '))
gender = input('Gênero: ').lower()

if (age > 0 and age < 150):
    print('Sua idade é:', age)
else:
    print('Idade inválida')

if (salary > 0):
    print('Seu salário é de:', salary)
else:
    print('Salário inválido')

if 'm' in gender:
    print('Você é do sexo masculino')
elif 'f' in gender:
    print('Você é do sexo feminino')
else:
    print('Informação inválida')
