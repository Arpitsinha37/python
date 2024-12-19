#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        idx=0
        curr=1
        while k> 0:
            if idx<len(arr) and arr[idx] == curr:
                idx+=1
            else:
                k-=1
                if k == 0 :
                    return curr
            curr+=1
        return curr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends