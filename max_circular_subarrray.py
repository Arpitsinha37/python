#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    total = 0
    max_sum = cur_max = float('-inf')
    min_sum = cur_min = float('inf')

    for i in arr:
        cur_max = max(i, cur_max + i)
        max_sum = max(max_sum, cur_max)

        cur_min = min(i, cur_min + i)
        min_sum = min(min_sum, cur_min)
        
        total += i

    return max(max_sum, total - min_sum, total)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends