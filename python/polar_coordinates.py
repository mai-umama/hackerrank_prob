import cmath # a module for complex numbers
z= complex(input()) #convert input into complex number

r = abs(z) # abs the tool that returns thje absolute value of complex number z

f = cmath.phase(z) #this tool returns the absolute value of phase means argument of z

print(r)
print(f)