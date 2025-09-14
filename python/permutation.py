from itertools import permutations #itertools is a library of python from which we import permutations

s,k = input().split() # (HACK) is s and (2) is k
k = int(k)

for p in sorted(permutations(s,k)): #every permutations stores in p variable the breif description is on notebook
    print("".join(p)) #convert the tuple into single string
    #permutations() always gives tuples
