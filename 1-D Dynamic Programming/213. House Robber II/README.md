# [213. House Robber II](https://leetcode.com/problems/house-robber-ii/description/) <span style="color:orange">Medium</span>

## **The Problem**
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array *nums* representing the amount of money of each house, return *the maximum amount of money you can rob tonight* **without alerting the police**.

## **Examples**
**Example 1**

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```
**Example 2**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
**Example 3**
```
Input: nums = [1,2,3]
Output: 3
```

## **The Solution**
For this solution, we want to implement the same algorithm for house robber 1 but we'll take the max of either the array skipping the first element or skipping the last element.
The algorithm itself goes through the array and uses rob1 & rob2 as n-2 & n-1. They both start off as 0 and we look for the max of n + (n-2) or (n - 1) and store it in our temp value. Next to go through the array, we assign rob1 which is (n - 2) to the next variable which is rob2 and then our rob2 as the temp value which contains our max. Then we return our rob2 which is the max.
Now, we pass our array to this algorithm running in our helper function but we want the max of three variables. Our first one is index of 0 if our arrray has only one element, next is our array but skipping our first element, and last is array without the last element. This is because we know we can't get the max including our first and last element since the houses are in a circle.

## **The Code**

```python
def rob(self, nums: List[int]) -> int:
    return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

def helper(self, num):
    rob1, rob2 = 0, 0

    for n in num:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
```