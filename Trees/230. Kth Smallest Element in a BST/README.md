# [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) <span style="color:orange">Medium</span>

## **The Problem**
Given the *root* of a binary search tree, and an integer *k*, return the *kth* smallest value (**1-indexed**) of all the values of the nodes in the tree.

## **Examples**
**Example 1**

![exampleImg](kthtree1.jpg)
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```
**Example 2**

![exampleImg](kthtree2.jpg)
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## **The Solution**
In this solution, to find the *kth* smallest value we'll travel down the left side of the tree and add those values to our list. We know the left side of the tree are the smaller values and will be creating a list from largest to smallest since we're appending values. Then one we reached the end, we'll go through our stack and pop off the last element until we've reached the *kth* value. Since we've reached k, we then return unless we haven't reached k then our current becomes the right element of our current. This would be our smallest value since we popped it off the list, so the right node will be larger than the current but smaller than the current's parent. We then do the same on that node and continue until we reach the end of k.

## **The Code**

```python
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    cur = root
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        
        if k == 0:
            return cur.val
        
        cur = cur.right

```