def string_formatting(number):
    width = len(bin(number))-2 # for right aligned each value and unprint the first 2 characters

    for i in range(1, number+1):
        deci = str(i).rjust(width) # only number, it done the space on left and allign on right
        octa = oct(i)[2:].rjust(width) #starts with 2 no index
        hexa = hex(i)[2:].upper().rjust(width)# ifhex(15) print f which is not corect for correction upper() is important print F
        bina = bin(i)[2:].rjust(width)
        print(deci, octa, hexa, bina)
if __name__ == '__main__':
    number= int(input())
    string_formatting(number) #function call at the place of number it can be anything like only n