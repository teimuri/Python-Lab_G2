#   "**" is the power
a=[2**i for i in range(17)] # prints all of the powers of 2 from 2^0 to 2^16
print(a)
b=[x*x for x in range(1,5)]# Prints X^2 for x between 1 to 4
print(b)
c=[a[x] for x in b if x%2==0]#prints a[n^2] for even n between 1 to 4
print(c)
