class Solution:
    def removeDuplicates(self, arr):
        # code here
        a=set()
        c=[]
        for i in arr:
            if i not in a:
                a.add(i)
                c.append(i)
            
        return c
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1
