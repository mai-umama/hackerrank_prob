def split_and_join(line):
    return "-".join(line) #takes each element of the list and joins them into a single string.
    #putting(-)between each element.

if __name__ == '__main__':
    line = (input().split()) #split is more important to make understand that there are word and 
                            #several strings not a single string
    result = split_and_join(line) # function call
    print(result)