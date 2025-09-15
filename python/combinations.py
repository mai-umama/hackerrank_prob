from itertools import combinations

s,k = input().split()
k = int(k)

for i in range(1,k+1): # From the characters, it generates all possible combinations of length = i
    for p in sorted(combinations(sorted(s),i)): # for print the single characters we need to sort the str first
                                                # like HACK -> ACHK
        print("".join(p))
