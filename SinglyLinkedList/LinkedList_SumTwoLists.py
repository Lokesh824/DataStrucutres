# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:05:26 2019

@author: INKUML05
"""

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
             print(curr.data,end='')
             curr=curr.next
         print('\n')
             
    '''
    We have two list here and we try to sum the values of linked list in the format 
    1 1    -- carrys 
    2 3 4
    5 6 7
    ------
    8  0  1   - answer
    -------
    
    '''
    def sum_List(self,List1):
        p = self.Head
        q = List1.Head
        print(p,'\n',q)        
        carry = 0
        ll = LinkedList()
        while p or q:
            if p:
                i = p.data
            else:
                i = 0 
            if q:
                j = q.data
            else:
                j = 0
            print('Resulting operations {0} + {1} + {2}'.format(i,j,carry))
            res = i+j+carry
            if res >= 10:
                carry = 1   
                rem = res // 10
                ll.append(rem)
            else:
                carry = 0
                ll.append(res)                
            if p:                        
               p=p.next
            if q:                
               q=q.next
                        
        ll.print_List()                 
           
             
LL = LinkedList()
LL.append(2)    
LL.append(3)
LL.append(4)
L1 = LinkedList()

L1.append(3)
L1.append(6)
L1.append(2)


print('\n Printing The Linked List...... \n')
LL.print_List()
L1.print_List()

LL.sum_List(L1)