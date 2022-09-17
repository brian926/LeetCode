# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) <span style="color:green">Easy</span>

## **The Problem**
Given the *root* of a binary tree, return its *maximum* depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

## **Examples**
**Example 1**

![exampleImg](tmp-tree.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2**

```
Input: root = [1,null,2]
Output: 2
```

## **The Solution**
We'll solve this problem with a recursive method. With this method, we step through the left and right side of the tree recursively while keeping the count of the depth we're currently on. Once we hit a node that is null, we return back the depth so our return will be the max between the left and right side. If the tree is empty, we'd return 0 because the depth is 0 and if it is a tree of one then we're be returning 1 so we can handle both cases.

## **The Code**

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        if not root: return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                    
    return dfs(root, 0)
```