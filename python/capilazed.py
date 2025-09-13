import os # os is a module which is not imported . firstly need to import the module
def solve(s):
    return " ".join(word.capitalize() for word in s.split(" ")) # it is also correct with s.title() but i test case 
    # failed so we need to write this

if __name__ == '__main__':
    fptr = open("output.txt", 'w') #on hackerrank output.txt is os.environ['OUTPUT_PATH'], 'w' 
    #cause the output file is already exist on hackerrank not in vscode so we first need to create output,txt
    s = input()
    result = solve(s)
    fptr.write(result+'\n') #ftpr is a file pointer object 
    #after write down the value of result it came down to next line(\n)
    fptr.close() #file colsed ***very important***