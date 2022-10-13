# [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) <span style="color:orange">Medium</span>

## **The Problem**
Given two integer arrays *preorder* and *inorder* where preorder is the preorder traversal of a binary tree and *inorder* is the inorder traversal of the same tree, construct and return the *binary tree*.

## **Examples**
**Example 1**

![exampleImg](tree.jpg)
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```
**Example 2**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## **The Solution**


## **The Code**

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root

```