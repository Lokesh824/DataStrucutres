# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:38:42 2019

@author: inkuml05
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.Head = None
    ## appending some data in the liked list, to view all the opeartins related to insertion check LinkedList.py file 
    def append(self,data):
        new_node = Node(data)
       ###if the head is not null ie there are some elements in the linked list
        if self.Head:
            curr_node = self.Head
        ###iterate through each node to reach the end node
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new_node
        else: 
            self.Head = Node(data)
            
    ## Printing the liked list       
    def print_list(self):
        print('Printing the data in the linked list-')
        curr_node = self.Head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next
            
    def Delete_Node(self, value):
        ''' There can be two possible case for deleting a node 
        1. The Node to be deleted is head.
        2. The Node to be deleted is not Head.'''
        ##checking for case 1 the node to be deleted is head.
        '''These steps should be done for case 1
        1. Make Head.Data as none and Make the head.next as head
        '''
        curr_node = self.Head
        if value == self.Head.data:           
            self.Head = curr_node.next  
            curr_node = None
        else:
            prev = None
            while curr_node and curr_node.data != value:
                prev = curr_node
                curr_node = curr_node.next                
            if curr_node is None:
                print('Element not Found in the linked list')
                return            
            prev.next = curr_node.next
            curr_node = None                                                                                    
        
            
llist = LinkedList()
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.print_list()
                
llist.Delete_Node(5)
llist.print_list()
        
            
        
    