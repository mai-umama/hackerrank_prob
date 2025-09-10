if __name__=='__main__':
    s = input()
    #any checks at least one character in s meets the condition
    # for loop is mendatoy for check every character of the string
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))