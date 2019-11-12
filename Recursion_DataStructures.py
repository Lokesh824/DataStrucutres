# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:46:14 2019

@author: INKUML05
"""

'''Recursion is breaking a problem in small problems...Here we have discussed the two examples,
one is calculating fibonacci number at nth position and the other is calculating the factorial of a given number'''

'''For ex we need to calculate the fibo of 5 we can use recurssion as below tree
                                         fib(5)
                                 /                   \
                              fib(4)                fib(3)
                            /        \              /   \
                       fib(3)       fib(2)       fib(2)  fib(1)
                       / \
                  fib(2)  fib(1) 


The above tree can be used to calculate the fibonacci number, here we have a problem ie recomputation is done
eg fib(3) is calculated twice, to optimize this further we can use dynamuic programming memoziation.

Store the value once computed and use them insted of computing again that is called memoziation

'''
import time
def fibo(num):
   
    if num == 1 or num == 2:
        return 1
    else:
        res = fibo(num-2)+fibo(num-1)
        return res    
        
## Memoziation to the current problem       
def fiboMem(num, memo):
    if memo[num] is not None:
        return memo[num]   
    if num == 1 or num == 2:
        return 1
    else:
        result = fiboMem(num-2,memo)+fiboMem(num-1,memo)
        memo[num] = result
        return result
        


def fact(num):
    if num==1:
        return 1
    return fact(num-1)*num


memo = [None] * 10
print('factorial is',fact(5))
start_time = time.time()
print('fibo number is',fibo(9))
print('Time taken with recurssion', time.time() - start_time)
start_time1 = time.time()
print('Fibonacci using Memoziation',fiboMem(9,memo))
print('Time taken with Memoziation', time.time() - start_time1)

##check which approach took the least time in execution

if time.time() - start_time > time.time() - start_time1:
    print('Memoziation is best approach')
else:
    print('Recurssion is best approach')
