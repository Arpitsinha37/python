class Solution:
    def maxSubArraySum(self,arr):
        maxi=current=arr[0]
        for i in range(1,len(arr)):
            current=max(arr[i],current+arr[i])
            if maxi<current:
                maxi=current
        return maxi

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()
