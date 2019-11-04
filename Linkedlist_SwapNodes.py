# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:38:49 2019

@author: inkuml05
"""

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
                ##print('Node is', pos_node, t)
                new_node.next = t.next
                t.next = new_node
                return
            else:
                Not_Exists_Flag = True
                t=t.next
                                                                                
        if Not_Exists_Flag == True:
           print('Node does not exists in Linked List')
           return
        
    def swap_node(self, ele1, ele2):        
        ## check if both the pos1 and pos2 to swap are not same
        if ele1 == ele2:
            return
        ##find the first node ie pos1
        prev1 = None
        curr_node1 = self.Head
        while curr_node1 and curr_node1.data != ele1:
            prev1 = curr_node1
            curr_node1 = curr_node1.next        
            
        prev2 = None 
        curr_node2 =  self.Head
        while curr_node2 and curr_node2.data != ele2:
            prev2 = curr_node2
            curr_node2 = curr_node2.next
            
        print('Prev node address to {0} is {1}'.format(ele1, prev1))   
        print('Prev node address to {0} is {1}'.format(ele2, prev2))
        
        print('Next node is', prev1.next)
        print('Next node is', prev2.next)
        
        ###check if the node exists
        if not curr_node1 or not curr_node2:
            return 
        
       ##check if the node have a prev node, if there is no prev node then it is head
        if prev1:
            prev1.next = curr_node2
        else:
            self.Head = curr_node2
            
        if prev2:
            prev2.next = curr_node1
        else:
            self.Head = curr_node1
        ##map the next pointer of the swapped nodes
        curr_node1.next, curr_node2.next = curr_node2.next, curr_node1.next
            

        
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
llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)
print('Printing the Current Linked List')
print('')
llist.print_linkedList()
##print('')
##print('Printing the Prepend List')
##llist.prepend(4)
##llist.insert_after(3,8)
### map the address of sec to first and third to second node and make third node next as none
##print('')
##print('Printing the final Linked List')
##llist.print_linkedList()

llist.swap_node(4,6)

print('Printing the Swaped Linked List')
llist.print_linkedList()