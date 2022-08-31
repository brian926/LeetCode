# 217. Contains Duplicate

## **The Problem**
Given an integer array *nums*, return *true* if any value appears **at least twice** in the array, and return *false* if every element is distinct.

### **Examples**
Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```
**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
```
**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## **The Solution**

We will first create a set, since Set items are unordered, unchangeable, and do not allow duplicates values. Then we will simply loop through the values in the array and test if that value is in the Set. If not, we will add it to the Set and if it is then we know we have a duplicate and we'll return true.

## **The Code**

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