# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/) <span style="color:orange">Medium</span>

## **The Problem**
Given an integer array nums, find a subarray that has the largest product, and return the *product*.

The test cases are generated so that the answer will fit in a 32-bit integer.

## **Examples**
**Example 1**

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
**Example 2**

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
## **The Solution**


## **The Code**

```python
def maxProduct(self, nums: List[int]) -> int:
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:
        vals = (curMax * n, curMin * n, n)
        curMax = max(vals)
        curMin = min(vals)
        res = max(res, curMax)
    return res
```