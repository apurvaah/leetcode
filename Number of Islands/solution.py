class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totalRows = len(grid)
        totalColumns = len(grid[0])
        
        count = 0
        
        for row in range(totalRows):
            for column in range(totalColumns):
                if grid[row][column] == '1':
                    self.dfs(grid, row, column)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)