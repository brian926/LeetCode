# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) <span style="color:green">Easy</span>

## **The Problem**
Given the *root* of a binary tree, invert the tree, and return its *root*.

## **Examples**
**Example 1**

![exampleImg](invert1-tree.jpg)
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2**

![exampleImg](invert2-tree.jpg)
```
Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3**
```
Input: root = []
Output: []
```

## **The Solution**
We'll use a recursive method for the solution in this problem. First is we test if there isn't a root. Otherwise we swap the right and left childern of the node. After, we'll go recursively down the left side of the tree which will swap all the right and left childern. Once that is completely swapped on the left side we'll go down the right side of the tree and swap everything on the right side.
What is happening here is we're going down all the right on the left side while swapping childern nodes. Once we get to the last left node, we swap the right side childern nodes until we reach to the last right sided node.

## **The Code**

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```