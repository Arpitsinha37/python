class Solution:
    def isLengthEven(self, head):
        temp= head
        count = 0
        if head == None:
            return 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count % 2 == 0
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
