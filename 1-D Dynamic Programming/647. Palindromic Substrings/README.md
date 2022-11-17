# [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/) <span style="color:orange">Medium</span>

## **The Problem**
Given a string *s*, return the number of **palindromic substrings** in it.
A string is a **palindrome** when it reads the same backward as forward.
A **substring** is a contiguous sequence of characters within the string.

## **Examples**
**Example 1**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```
**Example 2**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## **The Solution**
This problem uses the same solution as Longest Palindromic Substring, but uses a different method.
For this solution, we are going to put the palindromic substring algorithm into a helper function. This function takes an index and then expands left and right to check if it is a palidromic string. For every palidromic string, we are to our count in the function and then return that count. Our main function goes through our string and passes the index of our current index to our helper function along with a index plus one to count for even palindromic strings. We add our return to a result variable and then return that variable.

## **The Code**

```python
def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.helper(s, i, i)
            res += self.helper(s, i, i+1)
        return res

def helper(self, s, l, r):
    count = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1
    return count
```