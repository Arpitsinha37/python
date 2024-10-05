import sys
sys.setrecursionlimit(10**8)
from collections import deque

class Solution:
    def numIslands(self,grid):
        row, col = len(grid), len(grid[0])
        ones = [[i, j] for i in range(row) for j in range(col) if grid[i][j]]
        dir1 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        
        for x, y in ones:
            if grid[x][y] in {0, -1}:
                continue
            
            q = deque()
            q.append([x, y])
            count+=1
            
            while q:
                x, y = q.popleft()
                grid[x][y]=-1
                for x1, y1 in dir1:
                    x2, y2 = x+x1, y+y1
                    if -1<x2<row and -1<y2<col and grid[x2][y2]==1:
                        q.append([x2, y2])
                        grid[x2][y2]=-1
            
        return count
    
    
    
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))