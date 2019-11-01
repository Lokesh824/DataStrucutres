# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:28:45 2019

@author: INKUML05
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:51:33 2019

@author: INKUML05
"""

"""convert a int to binary """
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def Pop(self):
        return  self.items.pop()
    
    def get_stack(self):
        return self.items
    def is_empty(self):
        if self.items.count == 0:
            return True
        else:
            return False
    

##while remainder != 0:
###for x in range(len(number)):
def binary_converter(number):
    t= number
    while t >0:
        remainder = t % 2
        quotient = t // 2
        t = quotient
     
        s.push(remainder)
         

def print_binary():
    binary=''
    for x in range(0, len(s.get_stack())):
        binary += str(s.Pop())
    print('Binary representations is',binary)
    return binary

s = Stack()
number = 324
binary_converter(number)
print('The Binary rep for {0} is {1}'.format(number,print_binary()))
