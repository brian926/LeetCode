
# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/) <span style="color:orange">Medium</span>

## **The Problem**
Given an integer array nums, find the 
subarray
 which has the largest sum and return its sum.
 
## **Examples**
**Example 1**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
**Example 2**

```
Input: nums = [1]
Output: 1
```
**Example 3**
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

## **The Solution**
For this problem, we want to find the max from a subarray within the current array.
To start, we'll use our current Sum which would be 0 and our max Sum which starts at the first index of the array. If our current Sum is less than 0, we'll reset it to zero and then add the current array index in our for loop to it. This ensures our subarray moves if our first elements our negative. Then we place our max sum from its current value or from current sum. 

## **The Code**

```python
def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(curSum, maxSum)
        return maxSum
```