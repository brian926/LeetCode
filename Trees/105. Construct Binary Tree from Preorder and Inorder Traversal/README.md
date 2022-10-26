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
First, we pop off the first element of the preorder list which would be the root and pass that index in the inorder list.
Then with that index, we use that element as our root and pass the left as the preorder list along with everything left of that element in the inorder and do the same on the right side except with everything to the right of the element in the preorder array. This is because the preorder array alreay has the element popped off and we know everything to the left of the element in the inorder list would be on the left side of the tree and reserve on the right.
Then we have our tree and we can simply return root.

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