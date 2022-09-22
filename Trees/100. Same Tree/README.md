# [100. Same Tree](https://leetcode.com/problems/same-tree/) <span style="color:green">Easy</span>

## **The Problem**
Given the roots of two binary trees *p* and *q*, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## **Examples**
**Example 1**

![exampleImg](ex1.jpg)
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```
**Example 2**

![exampleImg](ex2.jpg)
```
Input: p = [1,2], q = [1,null,2]
Output: false
```
**Example 3**

![exampleImg](ex3.jpg)
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## **The Solution**
The method we'll use to see if two trees are the same is to compare the roots to each other and travel through the tree doing so. To do this, we'll use a recursive method but saying if we have a p and q then return if they are equal and if their childern nodes are equal. We'll check if their childern nodes are equal by passing the left and right nodes down the same method. At the end, we'll return if p and q are equal to None which means the trees are the same length. If this returns true, and all the nodes are equal then we return true otherwise false.

## **The Code**

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p and  q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p == None and q == None

```