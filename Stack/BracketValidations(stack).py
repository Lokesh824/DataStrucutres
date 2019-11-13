# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:56:18 2019

@author: INKUML05
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
    def is_empty(self):
        if self.items.count == 0:
            return True
        else:
            return False
    
s = Stack()
par = '[{()}]'
print('Available Elements in stack are..',s.get_stack())

def validate_match(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1=='[' and p2 == ']':
        return True
    else:
        return False
    
isBalanced = True
i = 0
while i < len(par) and isBalanced == True:
    bracket = par[i]
    
    if bracket in '{([':
        print('cureent value pushing ..', bracket)
        s.push(bracket)
    else:
        if s.is_empty():
            isBalanced = False
        else:
            if not validate_match(s.Pop(), bracket):
                isBalanced = False
    i = i+1
print('Available Elements in stack are..',s.get_stack()) 
if isBalanced == True:
    print('Proper code, all the brackets have closings')
else:
    print('Not a proper code')
            
            


