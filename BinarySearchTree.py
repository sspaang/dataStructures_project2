""" NOTE: Use this as a library 
! HOW TO USE: ในไฟล์หลัก ใช้ from name_of_this_file import * 
! ตัวอย่าง: from BinarySearchTree import * 
! เรียกใช้ได้เฉพาะฟังก์ชันที่ไม่มี _ หน้าชื่อฟังก์ชัน 
! ต้องมีไฟล์นี้อยู่ในโฟลเดอร์เดียวกับไฟล์หลักด้วยนะ
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            print(f"{val} is the root.")
        else:
            self._insert(val, self.root)      # recursive
        print(f"{val} has been added.")

    def _insert(self, value, cur_node):   # private function
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)        # recursive
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("The value already in the tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
    
    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0
    
    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height+1)
        right_height = self._height(cur_node.right, cur_height+1)
        return max(left_height, right_height)

    def search(self, val):
        if self.root is not None:
            return self._search(val, self.root)
        else:
            return False

    def _search(self, val, cur_node):
        if val == cur_node.value:
            return True      # print(f"{val} is in the tree!")
        elif val < cur_node.value and cur_node.left is not None:
            return self._search(val, cur_node.left)                 # move to the next node
        elif val > cur_node.value and cur_node.right is not None:
            return self._search(val, cur_node.right)                # move to the next node
        return False # print(f"{val} is not in the tree!")

    def find(self, value):      # returns the node with specified input value
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None
    
    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left is not None:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._find(value, cur_node.right)
    
    def delete(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        # returns the node with min value in tree
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current
        # returns the number of children for the specidied node
        def num_children(n):
            num_children = 0
            if n.left is not None: 
                num_children += 1
            if n.right is not None: 
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # case 1 (node has no children)
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        
        if node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child
            
            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right)
            node.value = successor.value
            self.delete_node(successor)

    def inorder(self, node):
        if  node is None:   # node is None
            return ""       # stop
        else:        
            return str(self.inorder(node.left)) + " " + str(node.value) + " " + str(self.inorder(node.right))