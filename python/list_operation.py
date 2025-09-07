n = int(input())
arr=[] #empty list

for i in range(n):
    command = input().split() #put the commands with using space

    if(command[0])=="insert":
       arr.insert(int(command[1]),int(command[2])) #1st command is key index and 2nd command is the value of index
    elif(command[0])== "print":
        print(arr) #just print the newest list
    elif(command[0])== "remove":
        arr.remove(int(command[1])) #remove the first occurance which is given
    elif(command[0]== "append"):
        arr.append(int(command[1])) #add the int at last 
    elif(command[0])=="sort":
        arr.sort() #sort with proper accending
    elif(command[0])== "pop":
        arr.pop() # delete the last int from the list 
    elif(command[0])== "reverse":
        arr.reverse() #just reverse the list if it is [1,2,3] then it will be [3,2,1]

