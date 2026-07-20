class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total_cells = m*n
        k = k%total_cells
        if k == 0:
            return grid
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                old_index = i*n+j
                new_index = (old_index + k)%total_cells
                new_r = new_index//n
                new_c = new_index%n
                ans[new_r][new_c] = grid[i][j]
        return ans