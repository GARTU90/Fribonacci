#!/usr/bin/env python3
#by juan.daniel.rangel.avilaq@gmail.com
#GNU/GPL License
#My first secuence

#fribonacci secuense
#a b c
# 1, 1, 2, 3, 5, 8, 13, 21
N=10
a=1
b=1
c=0
print(a)
print(b)
fibo=[]
for x in range(N+1):
	c=a+b
	b=a
	a=c
	fibo.append(c)
print(fibo)
