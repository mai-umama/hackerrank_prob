N = int(input())
country = set()# the set is empty here by the next add() method the elements added
for i in range(N):
    contries = input().strip() # strip is important cause if we input " uk " we nwwd "uk" without spaces strip function erase the spaces automiataclly
    country.add(contries) #add the countries on country set 

print(len(country)) # it don't be N cause python is not able to print the lenth of an integer