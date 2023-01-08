# Напишите программу, которая отсортирует список subject_marks по возрастаю оценок. 
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
# Sample Input:
# Sample Output:
# History 82
# English 88
# Science 90
# Physics 93
# Maths 97

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]

subject_marks = sorted(subject_marks, key = lambda x: x[1])

for i in subject_marks:
    print(i[0], i[1])