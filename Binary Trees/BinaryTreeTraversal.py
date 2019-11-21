# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:53:39 2019

@author: INKUML05
"""
"""
                1
              /   \
             2     3
            / \
           4   6
"""
class queue:
    def __init__(self):
        self.q = []
    
    def enquee(self,value):
        self.q.insert(0,value)
        
    
    def dequeu(self):
        if not self.is_empty():
            return self.q.pop()
        
    def is_empty(self):
        return len(self.q) == 0
    
    def __len__(self):
        c=0
        for x in self.q:
            if x is not None:
                c+=1
        return c

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

class BT:
    def __init__(self, root):
        self.root = Node(root)
        
        
    def print_tree(self):   
           print('\nDFS Tree traversals....\n')
           print('\nPreorder traversal....\n')
           self.preorder(self.root)
           print('\nPostorder traversal....\n')
           self.postordder(self.root)
           print('\nInorder traversal....\n')
           self.inorder(self.root)
                                
           print('\nThe level order traversal is...\n',self.level_order(self.root))
      
        
    def preorder(self,root):
        if root:    
                 
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)   
        
        else:
            print('Reached the end node....')
            
    def postordder(self,root):
        if root:
            self.postordder(root.left)
            self.postordder(root.right)
            print(root.data)
        else:
            print('Reached the end node....')
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
        else:
            print('Reached the end node....')
            
               
    '''In the level order traverse we will be using a Queue to hold the data of the poped node
    The Algorithm for level order traversal BFS...
    1. take the root node and add it in the queue
    2. pop the root,print it and check the left and right childrens of that and push them into queue
    3  repeat the process untill the queue is empty.
            '''
    def level_order(self, root):
        if root is None:
            return 
        else:
            q = queue()
            q.enquee(self.root)
            ##print('lenght is..', q.q_len())
            level = ''
            while len(q)>0: 
                    ##print('The length is ...',q.q_len())
                    last =  q.dequeu()
                    levelq = last.data
                    level = level + str(levelq)+' - '
                    print('\nThe last element poped from queue is..',last.data)
                    
                    Lchild = last.left
                    Rchild = last.right
                    print(Lchild)
                    print(Rchild)
                    q.enquee(Lchild)
                    q.enquee(Rchild)
                    
            
                    
  
        return level    
     
        
    
            
tree = BT(1)
tree.root.left= Node(2)
tree.root.right=Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.print_tree()

