X = int(input())
sizes =list(map(int,input().split()))
customers = int(input())
shop =[]
total_price= 0 #the price at first is 0

for i in range(customers):
    size,price = map(int ,input().split())
    
    shop.append((size,price))

    if size in sizes:#it findout the size in sizes list
        sizes.remove(size)   # ekbar sell hole remove
        total_price += price # tatal_price = tatal_price + price

print(total_price)