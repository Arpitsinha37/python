class Solution:
    def rotateDelete(self,  arr):
        arp=len(arr)
        for i in range(1,arp // 2 + 1):
            arr.insert(0,arr.pop())
            arr.pop(-i)
        return arr[0]
    
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1