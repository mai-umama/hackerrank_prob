N,M = map(int, input().split()) #length and width
#Top half
for i in range(N // 2):
    pattern = ".|." * (2 * i+1) #we always must use ascii code not unicode
    print(pattern.center(M,"-")) #put the pattern on middle and fill the gap with'-'

#Middle
print("WELCOME".center(M,"-"))

#bottom half
for i in range(N // 2-1,-1,-1): #reverse order N//2-1 is the star parameter, -1 stop and -1 step parameter
    pattern= ".|." * (2 * i + 1)
    print(pattern.center(M,"-"))