from itertools import  groupby # an iterable function that makes groups by following consecutive elements

S = input().strip() #remove the gaps from the input

for key, group in groupby(S): # key= character group = a collection of how many times the cha repeats
    count= len(list(group)) # first make a list where we have the elements of( if 2 repeats 3 times the list contain 3 twos)
                            #group , then calcualte the length 
    print((count,int(key)), end=" ") # count = how many times and key is character but convert it into int for the sake of perfect 
                                     # output ; end prevents the new line and print the modified sring in a single line
