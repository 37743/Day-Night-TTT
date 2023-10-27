# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Queue Data Structure
# ---
class Node:
    def __init__(self, value, move=0):
        self.value = value
        self.move = move
        self.next = None
 
class Queue:
    ''' Queue data structure'''
    def __init__(self):
        self.front = None
        self.size = 0
    
    def __str__(self):
        current = self.front
        string = ""
        while current:
            string += str(current.value) + " "
            current = current.next
        return string[:-1]
  
    def enqueue(self, value, move=0):
        new_node = Node(value, move)
        if self.front is None:
            self.front = new_node
        else:
            current = self.front
            while current.next != None:
                current = current.next
            current.next = new_node
        self.size += 1
 
    def is_empty(self):
        return self.size == 0

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        remove = self.front
        self.front = self.front.next
        self.size -= 1
        return remove.move
 
    def top(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self.front.value
 
    def get_size(self):
        return self.size