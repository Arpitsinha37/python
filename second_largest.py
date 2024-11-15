class Solution:
    def getSecondLargest(self, arr):
        a=list(set(arr))
        a.sort()
        if len(a)<=1:
            return -1
        else:
            return a[-2]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")