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
Much like the solution for Same Tree, we'll implement a function that checks if two trees are the same. This function takes two trees, and recursively returns back to itself if the values are equal and passes its left and right nodes. Once we get to the end of the trees, we return back if the last values are equal.
Our main function will first pass its values into the sameTree function to see if they are equal. Then we check if we have a root, and lastly we pass our left and right nodes of the main tree to the main function. This will check if the subtree exists on the left or right side of the main tree.

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