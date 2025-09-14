A = list(map(int,input().split()))

B = list(map(int,input().split()))

product =  [(a,b) for a in A for b in B ]
for r in product:
    print(r,end = " ")