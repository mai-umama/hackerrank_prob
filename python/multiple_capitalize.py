s = input()
indexes = list(map(int,input().split()))

char_list = list(s) # for sake of index we need to make the string into list

for index in indexes:
    if 0<= index < len(char_list):
        char_list[index]= char_list[index].upper()

new_text = ''.join(char_list) #again convert the list s into string 
print(new_text)