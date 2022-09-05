# 15. 3Sum <span style="color:orange">Medium</span>

## **The Problem**
Given an integer array nums, return all the triplets *[nums[i], nums[j], nums[k]]* such that *i != j, i != k*, and *j != k*, and *nums[i] + nums[j] + nums[k] == 0*.

Notice that the solution set must not contain duplicate triplets..

## **Examples**
**Example 1**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```
**Example 2**
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```
**Example 3**
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## **The Solution**
Within this problem, we will use two pointers on a sorted array to help find the triples. First we sort the array, this will help weed out duplicate values and help with our pointers. Then stepping through the array length, we assign our right most pointer to the end of the array while our left pointer is the next item in the array. While our left and right pointers are not equal, we check for combinations that equal 0. If the result is too small we move our left pointer to the right, else if too big we move our right pointer left. Else, this means the sum is 0 so we append our values and then cycle through our left pointer until we reach a non-duplicated value and run our checks again.

```
[-1,0,1,2,-1,-4]

[-4, -1, -1, 0, 1, 2]
[i[-4], j[-1], -1, 0, 1, k[2]]
[i[-4], -1, j[-1], 0, 1, k[2]]
[i[-4], -1, -1, j[0], 1, k[2]]
[i[-4], -1, -1, 0, j[1], k[2]]

[-4, i[-1], j[-1], 0, 1, k[2]]
append.[-1, -1, 2]
```

## **The Code**

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    out = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
            
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if (nums[i] + nums[j] + nums[k] < 0):
                j += 1
            elif (nums[i] + nums[j] + nums[k] > 0):
                k -= 1
            else:
                out.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
    return out
```