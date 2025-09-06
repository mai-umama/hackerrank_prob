N = int(input())
students =[]

for i in range(N):
    name= input()
    grade = float(input())
    students.append((name,grade))

grades = sorted({grade for _,grade in students})

second_lowest = grades[1]
#alphabetically sajay
names = sorted([name for name , grade in students if grade == second_lowest ])#it findout the second lowest student name
names.sort() #accending the second lowest names
for n in names:
    print(names)