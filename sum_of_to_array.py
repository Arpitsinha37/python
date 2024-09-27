class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        sum = 0
        for n in range(len(arr2)):
            sum = arr2[n] + sum
            if arr2[n] in arr1:
                for m in range(arr1.index(arr2[n])+1, len(arr1)):
                    sum = arr1[m] + sum
                if arr1[-1] not in arr2:
                    break
                else:
                    for o in range(arr2.index(arr1[-1])+1,len(arr2)):
                        sum = arr2[o] + sum
                    break
        return sum
    
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)   