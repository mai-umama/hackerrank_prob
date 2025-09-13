s =input()
index = int(input())

char_list = list(s)
char_list[index]= char_list[index].upper()

new_text = ''.join(char_list)
print(new_text)   
# this code is valid for only one string with one index