# [1. Two Sum](https://leetcode.com/problems/two-sum/) <span style="color:green">Easy</span>

## **The Problem**
Given an array of integers *nums* and an integer *target*, return *indices* of the two numbers such that they add up to *target*. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## **Examples**
**Example 1**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
**Example 2**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
**Example 3**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## **The Solution**
We know in the problem that there is exactly one solution and we cannot use the same element twice, so we start off with a dictionary to keep our key pairs. First we'll step through the array and find the difference of the element and target. If the difference is in our dictionary, then we can return that element and our dictionary value. Else, we add the element as the key and it's index as the value into our dictionary. This was when we return on a match, we return the index which is the value of the dictionary and the index of the element we current are on.

## **The Code**
### Python

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        test = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in test:
                return [test[target - nums[i]], i]
            test[nums[i]] = i
```

### JavaScript
```JavaScript
var twoSum = function(nums, target) {
    let test = new Map()
    
    for(let i = 0; i < nums.length; i++) {
        if (test.has(target - nums[i])) {
            return [test.get(target - nums[i]), i]
        }
        test.set(nums[i], i)
    }
};
```