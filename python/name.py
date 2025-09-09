def print_full_name(first, last):
    print("Hello" + first + " " + last + "! You just delved into python.")   
    #The value of first_name ("Ross") → goes into the function parameter called first.
    #The value of last_name ("Taylor") → goes into the function parameter called last.
    
if __name__== '__main__':
    first_name = input()
    last_name = input()
    print( first_name ,last_name)

#this code works correctly on hackerrank not in vscode

# def print_full_name(first,last):
#     first_name= first
#     last_name = last

# if __name__ == '__main__':
#     first= input()
#     last= input()
#     print("Hello",first,last ,"! you just delved into python")