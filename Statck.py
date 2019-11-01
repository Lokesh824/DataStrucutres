# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:04:11 2019

@author: inkuml05
"""

"""Stack DataStructure

"""
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def Pop(self):
        return  self.items.pop()
    
    def get_stack(self):
        return self.items
    
    
s = Stack()
s.push('A')
s.push('B')
s.push('c')
s.push('d')
s.push('e')
print('The elements in the stack-', s.get_stack())
print('Pop Operations')
s.Pop()
print('Reamining Elements are', s.get_stack())