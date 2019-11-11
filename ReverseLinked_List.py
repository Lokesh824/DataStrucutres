# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:20:09 2019

@author: inkuml05
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
##creating linked list
class LinkedList:
    def __init__(self):
        self.Head = None
    def append(self, data):
##new_node contains the address of node
        new_node = Node(data)
    ##case1: when there is no node existing
        if self.Head == None:
             self.Head = Node(data)
             return
    ##case 2: when there are some nodes existing in the documents then we need to iterate to the end and append the new node created 
        current_node = self.Head
        while current_node.next:
             current_node = current_node.next        
        current_node.next = new_node 
        
    def print_linkedList(self):
        t = self.Head
        print('Printing Head', self.Head)
        print('')
        while t:     
            print('|',t.data,'| ',t.next,'->', end=" ")
            t = t.next
           
    ##Driver program to reverse the given list
    '''A->B->C->D
       D->C->B->A
    '''        
    def reverse_LinkedList(self):
        prev = None
        curr = self.Head
        while curr:   
            print('\n')            
            ##storing the curr node in a temp
            t = curr.next  
            print('Link Part in the current node', t)
            print('next node for the current node', prev)
            ## Add the prev node add to the next part to curr node 
            curr.next = prev
            ## make current node as the prev node
            prev = curr         
            ## make current node as prev which is stored in temp variable
            curr = t  
            ##make the last node as the Head                  
        self.Head = prev

llist = LinkedList()
##add 3 nodes to the linked list
llist.append(45)
llist.append(224)
llist.append(323)
llist.append(432)
llist.print_linkedList()
print('\n')
print('Printing the reverse Linked list')
print('\n')
llist.reverse_LinkedList()
llist.print_linkedList()
