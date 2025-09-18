n = int(input())
N = set(map(int,input().split())) # make the input into a set

b = int(input())
B = set(map(int,input().split()))

set = N.union(B) # set union
print(len(set))