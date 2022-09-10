# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) <span style="color:orange">Medium</span>

## **The Problem**
Given an integer array *nums*, return an array *answer* such that *answer[i]* is equal to the product of all the elements of *nums* except *nums[i]*.

The product of any prefix or suffix of nums is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in *O(n)* time and without using the division operation.

## **Examples**
**Example 1**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]]
```
**Example 2**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## **The Solution**
This is question, we want to create an array that will have the product of all the input array except for the element of the same index in the input array. We'll use a prefix element that will start at 1, placed into the current index, and then be times by that index of the input array. This way, the next index will be the prefix of the values before it and not it self.

```python
Input = [1,2,3,4]
res = [1,1,1,1]

res[0] = 1(prefix)
prefix = 1 = 1(prefix) * 1(num[0])
res[1] = 1(prefix)
prefix = 2 = 1(prefix) * 2(num[1])
res[2] = 2(prefix)
prefix = 6 = 2(prefix) * 3(num[2])
res[3] = 6

res = [1,1,2,6]
```

Next we will step backwards through our array with a postfix, which will times the current index and then equal to itself times current input array index.

```python
Input = [1,2,3,4]
res = [1,1,2,6]

res[3] = 6 = 6(res[3]) * 1(postfix)
postfix = 4 = 1(postfix) * 4(num[3])
res[2] = 8 = 2(res[3]) * 4(postfix)
postfix = 12 = 4(postfix) * 3(nums[2])

res = [24,12,8,6]

```

Now our return array has all our answers with each index being products all of values except for the same index of itself in the input array. So our first past times all the values behind an index while our last past times all the values in front of an index.

## **The Code**

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prefix = 1
    
    for i in range(0, len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for x in range(len(nums) - 1, -1 , -1):
        res[x] *= postfix
        postfix *= nums[x]
        
    return res
```