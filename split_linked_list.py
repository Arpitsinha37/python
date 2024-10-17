class Node:
    def _init_(self, data):
        self.data = data
        self.next = None



class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        if not head:
            return [None, None]
        head1 = None
        head2 = None
        current1 = None
        current2 = None
        current = head
        index = 0
        while current:
            if index % 2 == 0:
                if head1 is None:
                    head1 = Node(current.data)
                    current1 = head1
                else:
                    current1.next = Node(current.data)
                    current1 = current1.next
            else:
                if head2 is None:
                    head2 = Node(current.data)
                    current2 = head2
                else:
                    current2.next = Node(current.data)
                    current2 = current2.next
                    
            current = current.next
            index += 1
        
        return [head1, head2]
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None



class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        if not head:
            return [None, None]
        head1 = None
        head2 = None
        current1 = None
        current2 = None
        current = head
        index = 0
        while current:
            if index % 2 == 0:
                if head1 is None:
                    head1 = Node(current.data)
                    current1 = head1
                else:
                    current1.next = Node(current.data)
                    current1 = current1.next
            else:
                if head2 is None:
                    head2 = Node(current.data)
                    current2 = head2
                else:
                    current2.next = Node(current.data)
                    current2 = current2.next
                    
            current = current.next
            index += 1
        
        return [head1, head2]
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])