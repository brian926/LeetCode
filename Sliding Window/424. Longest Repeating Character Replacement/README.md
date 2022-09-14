# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) <span style="color:orange">Medium</span>

## **The Problem**
You are given a string *s* and an integer *k*. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most *k* times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## **Examples**
**Example 1**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2**
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```
## **The Solution**
We'll be taking track of the count of each character, and increment them as we go through the string. Then we check if the length of the window we're using, from the left pointer to right pointer of the string, is larger than *k* if we minus the max count of values. This means if we minus the most common character, is there more characters left over than the amount of characters we can change to make the longest substring. If there is, we move our left pointer right to decrease our window and also decrease that character count. We then take the max of our max value or the size of our window, since our window is the length of strings where we can replace with *k*. Lastly, we return our answer once the loop is done.

## **The Code**

```python
def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        
        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r-l+1)
    return res
```