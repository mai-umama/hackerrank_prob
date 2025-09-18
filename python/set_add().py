N = int(input())
country = set()

for i in range(N):
    contries = input().strip()
    country.add(contries)

print(len(country)) # it don't be N cause python is not able to print the lenth of an integer