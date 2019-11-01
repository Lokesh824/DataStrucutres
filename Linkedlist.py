# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:08:50 2019

@author: INKUML05

"""
##creating a node sturcture ie wrapper
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
##creating linked list
class LinkedList:
    def __init__(self):
        self.Head = None
    
    def append(self, data):
##there can be two cases for adding new node
        '''1. There Is No nodes, so our new node will be the node
           2. There can be some elements so we need to iterate to the last to append to new node'''
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
                     
       
    def prepend(self, data):
          new_node = Node(data)          
          if self.Head != None:
              new_node.next = self.Head
              self.Head = new_node
            
##Traverse to the prevoius node given as pos_node, and point the pos_node.next to new node add and put the old value in pos_node.next into the new_node.next    
    def insert_after(self, pos_node, newd):
        new_node = Node(newd)
        Not_Exists_Flag = False
        t = self.Head
        
        '''check if the node before which new node to be inserted exists or not'''
        while t: 
            
            if t.data == pos_node:
                print('Node is', pos_node, t)
                new_node.next = t.next
                t.next = new_node
                return
            else:
                Not_Exists_Flag = True
                t=t.next
                                                                                
        if Not_Exists_Flag == True:
           print('Node does not exists in Linked List')
           return
       
##print the data in linked list
    def print_linkedList(self):
        t = self.Head
        print('Printing Head', self.Head)
        print('')
        while t:     
            print('|',t.data,'| ',t.next,'->', end=" ")
            t = t.next

##object for linked list class
llist = LinkedList()
##add 3 nodes to the linked list
llist.append(1)
llist.append(2)
llist.append(3)
print('Printing the Current Linked List')
print('')
llist.print_linkedList()
print('')
print('Printing the Prepend List')
llist.prepend(4)
llist.insert_after(3,8)
### map the address of sec to first and third to second node and make third node next as none
print('')
print('Printing the final Linked List')
llist.print_linkedList()
