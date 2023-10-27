# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Stack Data Structure
# ---
class Node:
    def __init__(self, value, move=0):
        self.value = value
        self.move = move
        self.next = None
 
class Stack:
    ''' Stack data structure'''
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def __str__(self):
        current = self.head.next
        string = ""
        while current:
            string += str(current.value) + " "
            current = current.next
        return string[:-1]
  
    def push(self, value, move=0):
        node = Node(value, move)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.move
 
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.head.next.value
 
    def get_size(self):
        return self.size