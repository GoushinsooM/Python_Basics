numbers = [1, 2, 4, 5, 8, 6, 96, 85, 73, 8, 2, 5, 1]
is_even = []

for number in numbers:
  number = number % 2
  if(number % 2 == 0):
    is_even.append(number)
  else:
    continue
    
print('Quantidade de pares: ', len(is_even))