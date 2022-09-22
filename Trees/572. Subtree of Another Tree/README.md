# [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) <span style="color:green">Easy</span>

## **The Problem**
Given the roots of two binary trees *root* and *subRoot*, return *true* if there is a subtree of *root* with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree *tree* is a tree that consists of a node in *tree* and all of this node's descendants. The tree *tree* could also be considered as a subtree of itself.

## **Examples**
**Example 1**

![exampleImg](subtree1-tree.jpg)
```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

**Example 2**

![exampleImg](subtree2-tree.jpg)

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

## **The Solution**


## **The Code**

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if self.sameTree(root, subRoot):
        return True
    if not root:
        return False
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def sameTree(self, l, r):
    if not (l and r):
        return l is r
    return l.val == r.val and self.sameTree(l.left, r.left) and self.sameTree(l.right, r.right)
```