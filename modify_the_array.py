class Solution:
       def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        for i in range(n-1):
            if arr[i] != 0 and arr[i] == arr[i+1]:
                arr[i] = arr[i]*2
                arr[i+1] = 0
                
        res = [num for num in arr if num!= 0]
        
        res.extend([0] * (n - len(res)))
        
        return res



if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1