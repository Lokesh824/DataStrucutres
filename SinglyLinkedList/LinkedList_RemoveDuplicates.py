# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:45:23 2019

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
             print(curr.data)
             curr=curr.next
    def remove_duplicates(self):
        occr_count = dict()
        curr = self.Head
        prev = None
        print('\n Printing Execution \n')
        while curr:            
            print('Checking if {0} is present in the linked list previously'.format(curr.data))
            if curr.data not in occr_count:
                print('{0} is not present in the list'.format(curr.data))
                occr_count[curr.data] = 1
                prev = curr
                
            else:
                print('{0} is Present in the list so removing it'.format(curr.data))
                prev.next = curr.next
                curr = None
                               
            curr = prev.next                
             
LL = LinkedList()
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)
LL.append(6)
LL.append(7)
LL.append(5)
LL.append(4)

print('\n Printing The Linked List...... \n')
LL.print_List()

LL.remove_duplicates()
print('\n Printing The Linked List after Duplicate Removal...... \n')
LL.print_List()
             
             
             
