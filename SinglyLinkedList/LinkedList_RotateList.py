# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:56:37 2019

@author: inkuml05
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
         print('| {0} | {1} |'.format(curr.data, curr.next),end=' -> ')
         curr=curr.next
     print('\n')
    
    
    '''
    The Given linked list should be rotated from the given position 
    example - 1-2-3-4-5-6-7
    and we give n as 4
    then the output should be
    5-6-7-1-2-3-4
    
    Algorithm:
        
        1.Store the head in some temp variable so that it can be used later
        2.Move from the first node to the nth node (n is the given rotation value)
        3.Then make the nth node next as none
        4.Make the n+1th node as head node
        5.Now iterate again and stop where the first null in next part occurs that is the rotated node end part
          and we should store in this inital head so that it will form a chain again
    
    
    '''
    def rotate_list(self, n):
        c=1
        temp_head = self.Head
        curr_node = self.Head
        while c<=n:         
            curr_node = curr_node.next
            c+=1
        new_head = curr_node.next
        curr_node.next = None
        self.Head = new_head
        
        new_curr = self.Head
        
        while new_curr.next:
            new_curr = new_curr.next
            break
        new_curr.next = temp_head
        return
        
       
        
            
            
    

LL = LinkedList()
LL.append(1)    
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)
LL.append(6)
LL.append(7)
LL.print_List()
LL.rotate_list(4)
LL.print_List()