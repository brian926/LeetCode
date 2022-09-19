# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) <span style="color:orange">Medium</span>

## **The Problem**
There is an integer array nums sorted in ascending order (with **distinct** values).

Prior to being passed to your function, nums is **possibly rotated** at an unknown pivot index *k (1 <= k < nums.length)* such that the resulting array is *[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]* **(0-indexed)**. For example, *[0,1,2,4,5,6,7]* might be rotated at pivot index *3* and become *[4,5,6,7,0,1,2]*.

Given the array *nums* **after** the possible rotation and an integer *target*, return the *index* of *target* if it is in *nums*, or *-1* if it is not in *nums*.

You must write an algorithm with *O(log n)* runtime complexity.

## **Examples**
**Example 1**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
**Example 2**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
**Example 3**
```
Input: nums = [1], target = 0
Output: -1
```

## **The Solution**
We know in this problem we have an sorted array that is pivoted at one point. To break this down, we want to binary search on either the left or right side as we know those are sorted from the pivot point.
The problem sets up with our two left and right pointers and we find our mid point. Knowing that if the the left pointer is less than the mid, we check our left side and see if the target is greater than our mid point or less than our left pointer. If it is, we know it can't be on the left side so we update our left pointer to mid plus 1. This is because we know our leftside would be a large half of the pivoted array while our right would be less. So if the target is smaller than our mid point or greater than our left most pointer it must then be on the left side of the array, we then update our right pointer to the mid pont minus one.
Otherwise, we check our right side of the array and if the target is smaller than our mid point or larger than our right pointer then it must be on the left side. The right pointer is updated as it should or if it doesn't meet the case we update our left pointer. 
Lastly, if we go through the entire array without a match we then return -1.

## **The Code**

```python
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1
```