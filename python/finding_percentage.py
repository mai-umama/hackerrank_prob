n = int(input())
students={} #empty dictionary

for i in range(n): 
    data = input().split() # for taking name and marks in one line
    name = data[0] # cause the index of name is 0
    marks = list(map(float,data[1:])) # marks indexs start with 1
    students[name]=marks

query = input() #specify the name
marks = students[query]

avg = sum(marks) / len(marks)
print("%.2f" %avg) #showing 2 places after the decimal