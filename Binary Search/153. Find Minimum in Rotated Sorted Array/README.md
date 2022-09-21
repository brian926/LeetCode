# [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) <span style="color:orange">Medium</span>

## **The Problem**
Suppose an array of length *n* sorted in ascending order is **rotated** between *1* and *n* times. For example, the array *nums = [0,1,2,4,5,6,7]* might become:

*[4,5,6,7,0,1,2]* if it was rotated *4* times.
*[0,1,2,4,5,6,7]* if it was rotated *7* times.
Notice that **rotating** an array *[a[0], a[1], a[2], ..., a[n-1]]* 1 time results in the array *[a[n-1], a[0], a[1], a[2], ..., a[n-2]]*.

Given the sorted rotated array *nums* of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in *O(log n)* time.

## **Examples**
**Example 1**
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```
**Example 2**
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```
**Example 3**
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
```

## **The Solution**
For this problem, we want to find the min of this rotated array and to do so we're use a binary search. This binary search is different since our array is rotated, meaning we have a sorted array with a midpoint which split it into a left and right side. To find the min, we'll use our usual left and right pointers and run our while loop. We'll get our midpoint by adding the pointers and dividing in half and then if the left pointer is less than our right we're place that into our min value else check if our mid is the min value. Lastly, we'll move our pointers to the half of the array that is smaller (left or right). If mid is larger than the left pointer we search the right half else the left. We've already stored our left pointer in the min value if it is the lowest else our right half of the array is the lower values.

## **The Code**

```python
def findMin(self, nums: List[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (r + l) // 2
        
        if nums[l] < nums[r]:
            res = min(res, nums[l])
        else:
            res = min(res, nums[mid])
            
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
            
    return res

```