# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:43:35 2021

@author: dell

"""


class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def length_ll(self):
        count=0
        if self.head==None:
            return 0
        itr=self.head
        while itr:
            count=count+1
            itr=itr.next
        return count
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head==None:
            self.insert_at_beginning(data)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node=Node(data,None)
            itr.next=node
                
    def insert_at_anypos(self,data,pos):
            if self.head==None and pos>1:
                raise 'INVALID INSERTION'
                    
            elif pos==1:
                return self.insert_at_beginning(data)
                
            elif pos==self.length_ll()+1:
                return self.insert_at_end(data)
                
            elif pos>self.length_ll()>+1:
                raise 'INVALID INSERTION'
                
            else:
                itr=self.head
                count=1
                while itr:
                    count=count+1
                    if count==pos:
                        itr.next=Node(data,itr.next)
                        return
                    itr=itr.next
            
            
    def remove_at(self,pos):
        if self.head==None and pos>=1:
            raise 'Invalid removal'
        elif pos==self.length_ll()+1:
            raise 'Invalid removal'
        else:
            if pos==1:
                self.head=self.head.next
                return
            count=1
            itr=self.head
            while itr:   
                count=count+1
                if count==pos:
                    itr.next=itr.next.next
                    return
                itr=itr.next
                
                    
        
    def print_ll(self):
        if self.head==None:
            print('No elements are there in the linked list')
            return
        itr=self.head
        while itr:
            print(itr.data,end=" ")
            itr=itr.next
            
    def insert_values(self,lst):
        for i in lst:
            ll.insert_at_end(i)
    
   
    def insert_after_value(self,data_after,data_to_insert):
        if self.head==None:
            raise 'INVALID OPERATION'
        
        itr=self.head
        flag=0
        while itr:
            if itr.data==data_after:
                node=Node(data_to_insert,itr.next)
                itr.next=node
                flag=1
                return
            itr=itr.next
        if flag==0:
            raise "Data doesn't exist"
                
    def remove_by_value(self,data):
        if self.head==None:
            raise 'INVALID OPERATION'
            

        if self.length_ll()==1 and self.head.data==data:
            self.head=None
            return 
        elif self.head.data==data:
            self.head=self.head.next
            return
        
        itr=self.head
        
        flag=0
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                flag=1
                return
            itr=itr.next
            
        if flag==0:
            raise 'INVALiD DATA'
                
    

ll=LinkedList()
ll.insert_values(['banana','apple','strawberry'])
ll.print_ll()
print()

ll.insert_at_anypos(12, 1)
ll.insert_at_anypos(11, 2)
ll.insert_at_anypos(13, 1)
ll.insert_at_anypos('blueberry', 5)
ll.print_ll()
print()

ll.insert_at_anypos(18, 4)
ll.insert_at_anypos(20, 3)
ll.print_ll()
print()

ll.remove_at(5)
ll.print_ll()
print()

ll.insert_after_value('banana','grapes')
ll.print_ll()
print()

ll.insert_after_value('strawberry','raghu')
ll.print_ll()
print()

ll.insert_after_value(13,14)
ll.print_ll()
print()

ll.remove_by_value(13)
ll.print_ll()
print()



'''
ll.insert_at_beginning(5)
ll.insert_at_beginning(10)
ll.insert_at_end(20)
print(ll.length_ll())
ll.insert_at_anypos(12, 2)
ll.insert_at_beginning(16)
ll.print_ll()

'''


        
        
        