# [338. Counting Bits](https://leetcode.com/problems/counting-bits/) <span style="color:green">Easy</span>

## **The Problem**
Given an integer *n*, return an array *ans* of length *n + 1* such that for each *i (0 <= i <= n)*, *ans[i]* is the **number of** *1*'s in the binary representation of *i*.

## **Examples**
**Example 1**

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```
**Example 2**

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

## **The Solution**
In this solution, we take the power of 2 and subtract that power from the number we are on and add a one to the difference. For example if we are on the number of 5, 2 to the power of 2 is 4 then (5-4) + 1 is 2 which is the total number of ones in 5 as binary.
First we start our array, and then go through the range of numbers. We check if we have a new offset by seeing if the number we're on is equal to the last offset times two, because any number after would be this new offset. Then we set that index in our array to the difference of the number and offset plus one. And to solve, we return our array.

## **The Code**

```python
def countBits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp

```