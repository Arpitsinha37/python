class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        curr, incre = -1, 0
        for arp in arr:
            if curr >= arp:
                curr += 1
                incre += curr - arp
            else:
                curr = arp
        return incre
