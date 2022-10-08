# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) <span style="color:orange">Medium</span>

## **The Problem**
Given the *root* of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.

## **Examples**
**Example 1**

![exampleImg](tree1.jpg)
```
Input: root = [2,1,3]
Output: true
```
**Example 2**

![exampleImg](tree2.jpg)
```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## **The Solution**
For this problem, we know the left side of the tree will always be less than root and the right side always larger than root. Otherwise, we will return false. In the solution we create our own check method which if that case isn't meet we return false. Then in the method, we recursively pass our left child, our left, and our current node value to check our left side and our node right, node value, and right for our right side. Our lefts will always be smaller and rights always greater otherwise it is not a binary search tree and vice versa for our right side. 
Lastly, to start we mass infinity and root to this method. The left side could be infinitely smaller than our root as well as our right being larger.

## **The Code**

```python
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs (node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
    return dfs(root, float("-inf"), float("inf"))
```