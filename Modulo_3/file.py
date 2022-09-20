#LEITURA DE ARQUIVO
#acessar arquivo
file = open('Modulo_3/src/dom_casmurro.txt', 'r')
text = file.read()
print(text)
file.close()

#acessar conteúdo linha a linha
file = open('Modulo_3/src/dom_casmurro.txt', 'r')
line = file.readline()
while line != '':
    print(line, end=' ')
    line = file.readline()
file.close()

file = open('Modulo_3/src/dom_casmurro.txt', 'r')
for line in file:
    print(line, end='')
file.close()

#fechar arquivo automaticamente
with open('Modulo_3/src/dom_casmurro.txt', 'r') as file:
  text = file.read()
  print(text)

#ESCRITA DE ARQUIVO
#WARNING: QUANDO FOR ESCREVER EM UM ARQUIVO TER CUIDADO PARA NÃO SOBRESCREVER UM EXISTENTE
with open('Modulo_3/src/teste.txt', 'w') as new_file:
  new_file.write('Novo arquivo criado e escrito por mim usando python!')

with open('Modulo_3/src/teste.txt', 'a') as new_file:
  new_file.write('Nova linha criada e escrita por mim usando python!')