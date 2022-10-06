# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) <span style="color:orange">Medium</span>

## **The Problem**
Given the *root* of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## **Examples**
**Example 1**

![exampleImg](tree1.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```
**Example 2**
```
Input: root = [1]
Output: [[1]]
```
**Example 3**
```
Input: root = []
Output: []
```

## **The Solution**


## **The Code**
### Python
```python
def containsDuplicate(self, nums: List[int]) -> bool:
        test = set()
       
        for i in nums:
            if i in test:
                return True
            else:
                test.add(i)
        return False
```
