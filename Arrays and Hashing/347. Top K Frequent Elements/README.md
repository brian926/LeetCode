# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) <span style="color:orange">Medium</span>

## **The Problem**
Given an integer array *nums* and an integer *k*, return the *k* most frequent elements. You may return the answer in **any order**.

## **Examples**
**Example 1**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
**Example 2**
```
Input: nums = [1], k = 1
Output: [1]
```

## **The Solution**
To tackle this problem, we want to create a heap that would store the number and the times they occur. We then use that heap to append the number to an array at the index of the count.
```
Input = [1, 1, 2, 2, 3]

heap = {1: 3, 2: 2, 3: 1}
arr = ["", 3, 2, 1, "", ""]
```
Now our list is ordered by the less frequent to the most. We then can create our return array and step backwards through our list and append the most frequent numbers until we reach *k*.

## **The Code**

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create heap
        freq = [[] for i in range(len(nums) + 1)] #create list size of array
        
        for n in nums: # for every number in array
            count[n] = 1 + count.get(n, 0) #add plus one of it in the heap
        
        for n, c in count.items(): #for each item of hash
            freq[c].append(n) #add to count that value
        
        res = [] #new list
        for i in range(len(freq) -1, 0, -1): #for number in range - 1 until 0 decreasing by -1
            for n in freq[i]: #for every value in each case for freq
                res.append(n) #add to list
                if len(res) == k: #if the len is k, time to return
                    return res
```