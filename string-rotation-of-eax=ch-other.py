#User function Template for python3

class Solution:
    
    #bangladeshi samjha kya kinaa sirf s1 ko aur s2 ko check kiya and sahi nahi nikla toh return false ya true hai toh s2 in s1+s2 bass.
    def areRotations(self,s1,s2):
        #code here

        if len(s1) != len(s2):
            return False
            
        return s2 in (s1 + s1)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends