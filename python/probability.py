from math import comb #compare to itertools math.comb is more easier for probablity
N = int(input())
elements = list(map(str,input().split())) #the list of the elements are string so str,input()
K = int(input()) #indices or elect the number of elements

count_a = elements.count('a') #how many a are there in list

total = comb(N,K) # The number of ways to choose K items from N items without considering the order.
# without considering the order mean if ( a, b) (b,a) the combination but it counts only one cause the elements are same so the combination
without_a = comb(N- count_a, K) # combinatioons of without a
at_least_1a = 1 - without_a /total # calculation of probability aminly it's a formual

print(at_least_1a)