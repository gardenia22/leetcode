class Solution:
    # @param {character[][]} grid
    # @return {integer}
    # def __init__(self):
        # self.direction = 
    def numIslands(self, grid):
        if not grid: return 0
        n = len(grid) + 2
        m = len(grid[0]) + 2
        grid = map(lambda row:['0']+row+['0'],grid)
        self.new_grid = [['0'] * m] + grid + [['0'] * m]
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if self.new_grid[i][j]=='1':
                    self.search(i,j)
                    ans += 1
        return ans

    def search(self, i, j):
        self.new_grid[i][j] = '0'
        for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
            if self.new_grid[x+i][y+j]=='1':
                self.search(x+i,y+j)

a = Solution()
islands = ["1011011"]
islands = []
print a.numIslands(islands)