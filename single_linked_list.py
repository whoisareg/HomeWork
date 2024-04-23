
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SingleLinkedList():
    def __init__(self, head):
        self.head = head
        
    def traverse(self):
        pahoc = self.head
        while pahoc is not None:
            print(pahoc.value)
            pahoc = pahoc.next
        
    
    def append(self, new_node):
        pahoc = self.head  
        while pahoc.next is not None:
            pahoc = pahoc.next    
        pahoc.next = new_node  
            
        
    def insert(self, new_node, index):
        pahoc = self.head
        current_index = 0
        if index == 0:
            new_node.next = pahoc
            self.head = new_node
        else:    
            while pahoc.next is not None and current_index < index - 1 :
                current_index += 1
                pahoc = pahoc.next
            new_node.next = pahoc.next
            pahoc.next = new_node   
        
            
            
                
        
   

_list = SingleLinkedList(Node(1))
_list.append(Node(9))
_list.append(Node(19))
_list.append(Node(29))
_list.insert(Node(7), 0)
_list.traverse()



