import csv

def read_file():
 with open('Modulo_3/src/alunos.csv', 'r', newline='') as student_list:
   reader = csv.reader(student_list, delimiter=',')
   for row in reader:
     print(row)
      
def copy_file(file_name, file_name_copy):
 with open(f'Modulo_3/src/{file_name}.csv', 'r', newline='') as student_list:
   reader = csv.reader(student_list)
   with open(f'Modulo_3/src/{file_name_copy}.csv', 'w', newline='') as copied_list:
     writer = csv.writer(copied_list)
     writer.writerows(reader)

read_file()
copy_file('alunos', 'alunos_media')

header = ['Media']
media_list = []
with open('Modulo_3/src/alunos_media.csv', 'r') as student_list:
  reader = csv.reader(student_list, delimiter=',')
  next(reader)
  for row in reader:
    grade_list = row[3:]
    grade_list = list(map(float, grade_list))
    media = sum(grade_list) / len(grade_list)
    media_list.append(media)
print(media_list)


with open('Modulo_3/src/alunos_media.csv', 'r') as student_list:
  reader = csv.reader(student_list, delimiter=',')
  with open('Modulo_3/src/alunos_media.csv', 'a', newline='') as student_media:
    writer = csv.writer(student_media)
    writer.writerow(header)
    writer.writerow(media_list)
