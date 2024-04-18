class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        #Traverse the grid
        for i in range(rows):
            for j in range(cols):
                #If it is a land block increment perimeter by 4
                if grid[i][j] == 1:
                    perimeter+=4

                    # check whether top neighbour is a land and then decrement by 2
                    if i>0 and grid[i-1][j] == 1:
                        perimeter -= 2

                    # check left neighbour is a land and decrement it by 2
                    if  j>0 and grid[i][j-1]==1:
                        perimeter -= 2
        return perimeter                
