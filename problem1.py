#!/usr/bin/python3

from itertools import product
row =  int(input('Enter number of rows: '))
column = int(input('Enter number of columns: '))

def factor(x):
	list1 = [i for i in range(1,x+1) if x % i == 0]
	return list1
print('All possible array combinations are: ')
for i in product(factor(row),factor(column)):
	print(i)
