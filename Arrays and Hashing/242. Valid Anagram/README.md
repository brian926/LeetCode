# 242. [Valid Anagram](https://leetcode.com/problems/valid-anagram/) <span style="color:green">Easy</span>

## **The Problem**
Given two strings *s* and *t*, return *true* if *t* is an anagram of *s*, and *false* otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## **Examples**
**Example 1**
```
Input: s = "anagram", t = "nagaram"
Output: true
```
**Example 2**
```
Input: s = "rat", t = "car"
Output: false
```

## **The Solution**

We are given two strings that we need to return true if they are an anagram and false otherwise. Since the first thing we know is that an anagram is formed by rearranging the letters, we check if the two strings have the same length. If they don't, we know they can never be anagrams.
Then we create some dictionaries(in Python), which we will use to store characters plus the number of times they occur. We already know both strings are the same length, so we can step through one string and increment the number of times it occurs. 
```python
countS = {
    "a": 3,
    "n": 1,
    "g": 1,
    "m": 1,
    "r": 1
}
countT = {
    "a": 3,
    "n": 1,
    "g": 1,
    "m": 1,
    "r": 1
}
```

Once finished, we can then simply compare the two dictionaries and return whether they are equal.

## **The Code**
```python
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```