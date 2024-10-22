class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        arp = 0
        curr = head
        while curr:
            arp+=1
            curr= curr.next
        curr = head
        for i in range(arp-n):
            curr = curr.next
        ans = 0
        while curr:
            ans += curr.data
            curr = curr.next
        return ans


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None