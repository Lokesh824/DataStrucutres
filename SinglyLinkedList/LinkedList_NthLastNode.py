# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:15:52 2019

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
    
    
    def Get_List_Length(self):
        curr = self.Head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count
            
    '''
       We need to find the nth last node 
       ex - 2-4-5-6-3-9
       and input n is 2
       then we need to get 3 because that is the 2nd the node in the linked list
       
       Algo:
           1. Get the length of the linked list 
           2. Sub the length from the n value, that gives the node to which we should traverse 
           3. Traverse to the destionation node and get the destionation.data and return the value.
       
    '''
    
    def find_nth_last_node(self, n):       
        length = self.Get_List_Length()
        print('The Length of the Linked List is {0}'.format(length))
        if n > length:
            print('The Given value is larger than the length of the list')
        elif n==0 or n<0:
            print('The given value is less than or equal to zero')            
        else:
            nodeToTraverse = (length - n)
            print('The Node to traverse is',nodeToTraverse)  
            current_node = self.Head
            counter = 0
            while counter != nodeToTraverse:
                current_node = current_node.next
                counter+=1
            print('Last node is', current_node)
            res = current_node.data
            return res
            
       
    
    
LL = LinkedList()
LL.append(1)    
LL.append(5)
LL.append(7)
LL.append(9)
LL.append(10)
LL.append(11)
LL.append(12)
LL.print_List()
r = LL.find_nth_last_node(3)
print('\n The 3rd last node is', r)