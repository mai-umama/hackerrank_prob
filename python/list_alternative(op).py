n = int(input())
my_list=[]

for i in range(n):
    command = input().split()

    if(command[0])=="append":
        my_list.append(int(command[1]))
    elif(command[0])=="sort":
        my_list.sort()
    elif(command[0])== "count":
        print(my_list.count(int(command[1]))) # how many times the inserted value exist
    elif(command[0])== "index":
        print(my_list.index(int(command[1]))) #the index of the inserted value
    elif(command[0])== "print":
        print(my_list)

if((len(my_list)!= 0) and (any (x %2 == 0 for x in my_list))) and (my_list == sorted(my_list)):
    print("Success")

else:
    print("Try again")

#if the value some how doesn't exist following the index command we can print -1 by using conditions
# -1 means the value is not available in the list. >=0 means avaiable