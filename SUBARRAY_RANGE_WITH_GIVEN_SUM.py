class Solution:
    def subArraySum(self,arr, tar):
        d={0:1}
        count=0
        cur_sum=0
        for i in range(len(arr)):
            cur_sum+=arr[i]
            if cur_sum-tar in d:
                count+=d[cur_sum-tar]
            d[cur_sum]=d.get(cur_sum,0)+1
        return count

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        t -= 1