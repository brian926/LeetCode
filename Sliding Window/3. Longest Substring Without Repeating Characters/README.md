# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) <span style="color:orange">Medium</span>

## **The Problem**
Given a string *s*, find the length of the **longest substring** without repeating characters.

## **Examples**
**Example 1**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## **The Solution**
First we'll start by creating a python so we have store multiple items in a single variable.
We'll start our left pointer at the beginning and our answer as 0. Then we'll step through the range of the array, which will be our right pointer. As we go through, we'll add the character to the set but if it is already in the set then we'll move our left pointer to the right. Our answer will be the max of either the answer variable or the current distance between the left and right pointers.
```
"abcabcbb"

LR[a]bcabcbb
char = "a"

L[a]R[b]cabcbb
char = "ab"

L[a]bR[c]abcbb
char = "abc"

aL[b]cR[a]bcbb
char = "bca"
```

## **The Code**

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
```