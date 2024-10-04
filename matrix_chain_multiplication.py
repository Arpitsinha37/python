class Solution:
    def matrixMultiplication(self, N, arr):
        dp=[[None for i in range(N)] for i in range(N)]
        for i in range(0, N-1):
            dp[i][i+1]=0
        for gap in range(2, N):
            for i in range(0, N-gap):
                j=i+gap
                dp[i][j]=float('inf')
                for k in range(i+1, j):
                    dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j])
        return dp[0][N-1]
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))