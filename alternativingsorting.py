class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        b = arr[::-1]
        ac = []
        for i in range(len(arr)):
            if i%2==0:
                ac.append(b[i//2])
            else:
                ac.append(arr[i//2])
        return ac
class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        b = arr[::-1]
        ac = []
        for i in range(len(arr)):
            if i%2==0:
                ac.append(b[i//2])
            else:
                ac.append(arr[i//2])
        return ac