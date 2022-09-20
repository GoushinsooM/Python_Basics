counter = 0

while True:
  if counter < 10:
    counter += 1
    multiplication_table = counter * 9
    print(f'9 * {counter} = ', multiplication_table)
  else:
    break