# [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) <span style="color:orange">Medium</span>

## **The Problem**
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).

## **Examples**
**Example 1**

![exampleImg](binarysearchtree_improved.png)
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```
**Example 2**

![exampleImg](binarysearchtree_improved.png)
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```
**Example 3**


```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

## **The Solution**
In this solution, we want to find the root of two given nodes. With a binary search tree, we know all nodes on the left are less than the parent node while on the right is larger. Knowing this, we know that if both nodes are less than the current node they are on the left side and vice versa if they are larger. With a while look, we'll move our current node right or left depending if the nodes are larger or small. Otherwise, if the current node is less than one node and greater than the other it is the common ancestor of those nodes.

## **The Code**

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    cur = root
    
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else: 
            return cur

```