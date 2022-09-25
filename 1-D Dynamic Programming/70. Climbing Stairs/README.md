# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) <span style="color:green">Easy</span>

## **The Problem**
You are climbing a staircase. It takes *n* steps to reach the top.

Each time you can either climb *1* or *2* steps. In how many distinct ways can you climb to the top?

## **Examples**
**Example 1**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
**Example 2**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## **The Solution**
In this problem, we know that the total number of ways to get to *n* stairs would be *[n-1]* and *[n-2]* since we could take either a single step to reach *n* or two steps to get there. This is just like fibonacci's numbers and we'll use the same method to solution the problem.
We'll start at steps 1 and for the range of *n*, minus one since we're starting at step 1, our answer would be *[n-1] + [n-2]*. 
```
n = 5
8,5,3,2,1,1
8 possible solutions for 5 steps
```
Then we would just return our answer once we've gone through the range of given *n*.

## **The Code**

```python
def climbStairs(self, n: int) -> int:
    one, two = 1, 1
        
    for i in range (n - 1):
        temp = one
        one = one + two
        two = temp
    return one
```