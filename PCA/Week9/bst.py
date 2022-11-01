class Node:
    def __init__(self, username_in, password_in):
        # your code here
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, new_node):
        if (self.root is None):
            self.root = new_node
        else:
            self.__insert_node(self.root, new_node)
            
    def __insert_node(self, current_node, new_node):
        if (new_node.username <= current_node.username):
            if (current_node.left is not None):
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif (new_node.username > current_node.username):
            if (current_node.right is not None):
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node
    
    def find(self, username):
        return self.__find_node(self.root, username)
    
    def __find_node(self, current_node, username):
        pass
        # your code here
        
    def remove(self, username):
        pass
        # your code here
    def is_empty(self):
        pass
        # your code here
        
    def preorder(self):
        pass
        # your code here
        
    def inorder(self):
        pass
        # your code here
        
    def postorder(self):
        pass
        # your code here
        
    def print(self):
        pass
        # your code here