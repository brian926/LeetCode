# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) <span style="color:orange">Medium</span>

## **The Problem**
Given an *m x n* 2D binary grid *grid* which represents a map of *'1'*s (land) and *'0'*s (water), return the *number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## **Examples**
**Example 1**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```
**Example 2**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

## **The Solution**
This solution uses Depth First Search to look through the entire graph for islands.
We travel through the entire graph and if we find a 1, we then convert all 1's into '#' until we hit water/a 0. Then we return and increase our counter by 1.
In the dfs, we are recursively looking through the graph from the start point and searching it's neighbors.

## **The Code**

```python
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
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
```