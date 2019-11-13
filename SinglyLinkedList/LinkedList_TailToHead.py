# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:18:00 2019

@author: INKUML05
"""
'''Moving the tail to head node'''
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
class LinkedList:
    def __init__(self):
        self.Head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.Head is None:
            self.Head = new_node
        else:
            curr_node = self.Head
            while curr_node.next:
                curr_node = curr_node.next            
            curr_node.next = new_node

    def print_List(self):
         curr =  self.Head
         while curr:
             print('| {0} | {1} |'.format(curr.data, curr.next),end=' -> ')
             curr=curr.next
         print('\n')

    '''Move the tail node to the head node ...
    Steps
    1. Store the head in temp variable
    2. Move to the last node 
    3. Make the head to point at the last node 
    4. Now the last node will be trated as fist node in the next part of new first node insert the temp value which we stored in step 1
    5. Now make the prev ie 2nd last node next value as None
    '''
    def tail_to_head(self):
        curr = self.Head        
        t = curr
        ##print('Inintal head', t)
        prev = None
        while curr.next: 
            prev = curr
            curr = curr.next          
        ##print('previous',prev)            
        ##print('Previous after operation', prev.next)
        self.Head = curr
        ##print('HEad npode', curr.data)
        ##print('tvalue', t)
        self.Head.next = t
        prev.next = None  
     

        
  

LL = LinkedList()
LL.append(2)    
LL.append(3)
LL.append(4)
LL.print_List()
LL.tail_to_head()
LL.print_List()