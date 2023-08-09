print("Hello, world")
students = ['Симоненко', 'Косач', 'Павлюк', 'Ковальчук', 'Сидоренко', 'Гончар']
# сортування списку учнів
students.sort()
# всього учнів
amount_students = len(students)
i = 1
print('Список класу:')
for student in students:
     print (i, '-', student)
     i += 1
print ('Всього учнів:', amount_students)