# [198. House Robber](https://leetcode.com/problems/house-robber/description/) <span style="color:orange">Medium</span>

## **The Problem**
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night.**

Given an integer array *nums* representing the amount of money of each house, return the **maximum amount of money you can rob tonight without alerting the police.**

## **Examples**
**Example 1**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
**Example 2**

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## **The Solution**
We want to setup our values for [j, k, n, n+1, n+2] where j if the first house while k is the second. The values are suppose to represent k as the last house while j is the houses before than. Thus, we start off both values as 0 since no houses were robbed. Then we find the max of the current house plus 2 houses ago since we can't rob the last house versus the last house.
This means j will become k, since k is the current and k will become the max. For example, in [2,7,9,3,1] the max between j+n where j,k=0 would be 2. J will become 0, which is two houses ago since no houses were robbed and k will become 2 since robbing the first houses is the max you can get. Then we find the max of j+n vs k which is 0+7 vs 2, again j will become 2 since that was two houses ago and k will become 7 because the max of the first two houses would be 7. This time j+n vs k is 2+9 vs 7, which you can see is house 1 and 3 vs house 2, now j become 7 since that was the last house while k is 11 because thats the max of house 1 and 3. Now, 7+3 vs 11 which both equals 11 and now both j and k are 11 since robbing house 1 & 3 and house 2 & 4 would equal 11. And lastly, 11+1 vs 11 would give us the max of 12 which would become k which we then return back.

## **The Code**

```python
def rob(self, nums: List[int]) -> int:
        j, k = 0, 0
        
        for n in nums:
            temp = max(n+j, k)
            j = k
            k = temp
        
        return k
```