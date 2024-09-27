import heapq
class Solution:
    def minCost(self, arr):
        s = 0
        heapq.heapify(arr)
        
        while len(arr) > 1:
            
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            s += first + second
            
            heapq.heappush(arr, first + second)
            
        return s
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))