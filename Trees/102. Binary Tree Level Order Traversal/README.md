# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) <span style="color:orange">Medium</span>

## **The Problem**
Given the *root* of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## **Examples**
**Example 1**

![exampleImg](tree1.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```
**Example 2**
```
Input: root = [1]
Output: [[1]]
```
**Example 3**
```
Input: root = []
Output: []
```

## **The Solution**
For this solution, to level order traversal we'll go through each level starting at root and read the nodes left to right. First, we're appending each value on the current level we are on. Once appended, we then need to go down one level and set this as our next level in our while statement. We do this by checking each node on the current level for a child (first left side and then right) and if so we add it so that this will be our next list to check. Now this level, which is made up of the childern nodes of the above level gets appended to our answer list and we're already in left to right order.

## **The Code**
### Python
```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        level = [child for node in level for child in (node.left, node.right) if child]
    return ans
```
