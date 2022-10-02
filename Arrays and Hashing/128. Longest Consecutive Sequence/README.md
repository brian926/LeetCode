# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) <span style="color:orange">Medium</span>

## **The Problem**
Given an unsorted array of integers *nums*, return the *length of the longest consecutive elements* sequence.

You must write an algorithm that runs in *O(n)* time.

## **Examples**
**Example 1**

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2**

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

## **The Solution**
Since we want the longest consecutive sequence, we're going to convert the list into a set and drop any duplicates. Then our method for this problem would be, if the number's previous number is not in the set then we know it is the start of a sequence. We then check if the next number is in the set and if it is then increase by one. And to find the longest sequence we check the max of a value and the current seqeunce we're in. Once we know we have the max in the max value and we've gone through the list, we return our max value.

## **The Code**
### Python
```python
def longestConsecutive(self, nums: List[int]) -> int:
    setOfList = set(nums)
    best = 0
    for x in setOfList:
        if x-1 not in setOfList:
            y = x + 1
            while y in setOfList:
                y += 1
            best = max(best, y - x)
    return best
```
### JavaScript
```JavaScript
var longestConsecutive = function(nums) {
    const newSet = new Set(nums)
    let maxScore = 0
    
    for (let num of [...newSet]) {

        let prev = num - 1
        if (newSet.has(prev)) {
            continue
        }

        let [cur, score] = [num + 1, 1]
        while (newSet.has(cur)) {
            cur++
            score++
        }
        
        maxScore = Math.max(maxScore, score)
    }
    return maxScore
};

```