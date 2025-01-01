#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        from collections import defaultdict
        anagram_map = defaultdict(list)
        
        # Group anagrams by sorted tuple of characters
        for word in arr:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        # Prepare the result in order of appearance and sorted lexicographically
        result = []
        for key in anagram_map:
            result.append(anagram_map[key])
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends