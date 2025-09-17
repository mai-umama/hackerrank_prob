A = list(map(int,input().split()))

B = list(map(int,input().split()))

product =  [(a,b) for a in A for b in B ]
#print(*product) if we write this line the ouput will bw also correct
for r in product:
    print(r,end = " ") #end means prevent the output go doem next line and print them one after another