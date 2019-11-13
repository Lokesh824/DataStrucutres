# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:51:52 2019

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
         
    '''We have two sorted lists and we need to merge those lists     
     List 1 = 1-5-7-9-10-11-12
     List 2 = 2-3-4-6-8
    
    Algo:
        
    1. Store the Head of List1 as p
    2. Store the Head of List2 as q
    3. Create a var s that points to the minimum value 
    4. check if p<q
        4.1 if yes then make s as p and move p to the next node
        4.2 if no then make s as q and move q to next node    
    5. Now loop and repeat the process of finding the minimum value and return the head of the merged list
    6. When any of the list comes to the last node then make the s.next to the other node.
    '''     
    def merge_List(self, List2):
        p =  self.Head
        q = List2.Head
        s = None        
        
        if not q:
            return p
        if not p:
            return q               
        
        if p.data<=q.data:
            print('\n {0} is lesser than the {1} and now s points to {2}, p points to {3} \n'.format(p.data,q.data,p, p.next))
            s=p
            p=p.next            
        else:
            print('\n {0} is lesser than the {1} and now s points to {2}, p points to {3} \n'.format(q.data,p.data,q, q.next))
            s=q
            q=q.next                       
        newHead = s
        
        print('\n New Head is {0}\n'.format(newHead))        
        while p and q:                            
            if p.data <= q.data:
                print('\n Now S.Next is {0} \n'.format(p))
                s.next = p
                p=p.next
                s=s.next 
                
                print('\n Appending node {0}'.format(s.data))
            else:
                print('\n Now S.Next is {0} \n'.format(q))
                s.next = q               
                q=q.next
                s=s.next 
                print('\n Appending node {0}'.format(s.data))
        if not p:
             
             s.next = q
             print('\n Now S.Next is {0} And the Rest of nodes are in List 1 so appending them as they are..\n'.format(s.next))
        if not q:
             
             s.next = p                                          
             print('\n Now S.Next is {0}  And the Rest of nodes are in List 2 so appending them as they are..\n'.format(s.next))    
        return newHead                                             

LL = LinkedList()
LL.append(1)    
LL.append(5)
LL.append(7)
LL.append(9)
LL.append(10)
LL.append(11)
LL.append(12)
L1 = LinkedList()
L1.append(2)
L1.append(3)
L1.append(4)
L1.append(6)
L1.append(8)

print('\n')
LL.print_List()
L1.print_List()
LL.merge_List(L1)
LL.print_List()