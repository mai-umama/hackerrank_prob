from itertools import combinations_with_replacement #without maintain the serial repeat the elements

s,k = input().split()
s = ''.join(sorted(s)) # we need to sort the str first otherwise the output result doesn't match with the test cases
k = int(k)

for p in sorted(combinations_with_replacement(s,k)):
    print("".join(p))

#combination with replacement diye we got more than 4 result output. AA CC HH KK . jwhich doesn't exist on combination module 