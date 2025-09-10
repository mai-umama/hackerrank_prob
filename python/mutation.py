def mutable_string(string,position,character):
    l =list(string) #convert the string into list so that it can access single character through index
    l[position] = character 
    return ''.join(l) #conver the element of the list into string
if __name__ == '__main__':
    s = input()
    l =list(s)
    i ,c = (input().split())
    s_new = mutable_string(s, int(i),c) #mainly func call s means string ,int(i) means position,c means character
    #the return value of the function placed at the location where fuction is called
    print(s_new)