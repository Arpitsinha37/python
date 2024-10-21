class Solution:
    def sameOccurrence(self, arr, x, y):
        count = 0
        diffMap = {0: 1}
        countX = 0
        countY = 0

        for num in arr:
            if num == x:
                countX += 1
            if num == y:
                countY += 1
            
            diff = countX - countY
            
            count += diffMap.get(diff, 0)
            diffMap[diff] = diffMap.get(diff, 0) + 1

        return count
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1