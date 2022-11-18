# [91. Decode Ways](https://leetcode.com/problems/decode-ways/description/) <span style="color:orange">Medium</span>

## **The Problem**
A message containing letters from *A-Z* can be encoded into numbers using the following mapping:
```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```
To **decode** an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, *"11106"* can be mapped into:

* *"AAJF"* with the grouping *(1 1 10 6)*
* *"KJF"* with the grouping *(11 10 6)*

Note that the grouping *(1 11 06)* is invalid because *"06"* cannot be mapped into *'F'* since *"6"* is different from *"06"*.
Given a string *s* containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.


## **Examples**
**Example 1**

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```
**Example 2**

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

***Example 3**
```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

## **The Solution**
We first start by declaring a dic that is 1 at the index of the string length, so for example *12* would be *{2: 1}*. Using a dfs function, we first pass 0 to it since we don't know of any solutions. Our goal is to use the dp Dic to store the number of solutions that we know for the string. 
In the dfs function, we check if *i* is in dp or if it is equal to *0* in the string. Then we get result from passing *i + 1* into the dfs function recursively. Since the only value in dp is the length of string, we go through until we hit the length and then return 1 and then *i* would be length - 1 so in our example *1*. Then we check if *i + 1* is less than the string length, if that index in the string is 1 or 2, and if the next index is 0-6 as we can use it as double digit solution. In our case it is none of those, so we add our result to the *i* index of dp, creating *{2: 1, 1: 1}*. Next we return result which is *1* back to the base recursive call where *i = 0*, and we run our if statement again. This time since index is 1 and the next value can be used as a double digit we add dfs(i+2) to our result and since 2 is in our dp Dic we return 1 back. We repeat adding it to dp so it is now *{2: 1, 1: 1, 0: 2}* with index 0 being the total of our results.

## **The Code**

```python
def numDecodings(self, s: str) -> int:
    dp = {len(s) : 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        
        res = dfs(i + 1)
        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            res += dfs(i + 2)
        dp[i] = res
        return res

    return dfs(0)
```