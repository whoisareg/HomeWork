
class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def __gt__ (self, other):
        return self.value > other.value
    
    def __lt__ (self, other):
        return self.value < other.value
        
class BinaryTree():
    def __init__(self, root:Node):
        self.root = root
        
    def add(self, new_node):
        current_node = self.root
        
        while current_node is not None:
            if current_node.value > new_node:
                if current_node.left is None:
                    break
                else:
                    current_node = current_node.left
            elif current_node.value < new_node:
                if current_node.right is None:
                    break
                else:
                    current_node = current_node.right
            else:
                return False        
        
        if current_node.value < new_node:
             current_node.right = Node(new_node)
        
        else:
            current_node.left = Node(new_node)
        
        return True
    
    def find(self, value):
        current_node = self.root
        
        while current_node is not None:
            if current_node.value == value:
                return current_node
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return None
        
        
    def delete(self, value):
        parent = None
        current = self.root
        
        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:  
            return False

        if current.left is None and current.right is not None:
            if parent is None:  
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.left is not None and current.right is None:
            if parent is None:  
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        elif current.left is not None and current.right is not None:

            min_larger_node_parent = current
            min_larger_node = current.right
            
            while min_larger_node.left is not None:
                min_larger_node_parent = min_larger_node
                min_larger_node = min_larger_node.left

            current.value = min_larger_node.value  

            if min_larger_node_parent.left == min_larger_node:
                min_larger_node_parent.left = min_larger_node.right
            else:
                min_larger_node_parent.right = min_larger_node.right

        else:
            if parent is None:  
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None


        return True
                
                            
    def traverse(self, current):
        if current.left is None and current.right is None:
            print(current.value)
            return
        if current.left is not None:
            self.traverse(current.left)
        print(current.value)
        if current.right is not None:
            self.traverse(current.right)      
   
        
tree = BinaryTree(Node(16))

tree.add(11)
tree.add(13)
tree.add(12)
tree.add(14)
tree.add(15)
tree.add(8)
tree.add(2)
tree.add(21)
tree.add(24)
tree.add(17)
tree.add(19)
tree.add(27)
tree.add(99)

found_node = tree.find(21)
print(f"Founded node is: {found_node.value}")

tree.delete(17)

tree.traverse(tree.root)

         