class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        s1=list(s1)
        s2=list(s2)
        s1.sort()
        s2.sort()
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True
if __name__ == '__main__':
    t = int(input("enter number of test cases:"))
    for i in range(t):
        a = input("enter first string:").strip()
        b = input("enter second string:").strip()
        
        solution=Solution()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        