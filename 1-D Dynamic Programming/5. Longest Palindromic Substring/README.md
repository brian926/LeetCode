# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/) <span style="color:orange">Medium</span>

## **The Problem**
Given a string *s*, return the longest palindromic substring in *s*.

## **Examples**
**Example 1**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
**Example 2**

```
Input: s = "cbbd"
Output: "bb"
```

## **The Solution**
The solution for this problem is to iterate through the string and at the given point expand left and right to determine if it is a palindromic. Then we store the length and substring into values and return the max.
First we go through the string and run two while loops. Our first loop will be at the current index of the for loop for odd palindromics and then expand our left and right window while storing the values. The next loop is for even palindromics, and we start our right pointer as the next element in the string and perform the same operations. Lastly, we return our result would be the max palindromic substring we found in the string while looking for odd and even palindromics.

## **The Code**

```python
def longestPalindrome(self, s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res
```