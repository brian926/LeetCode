# 191. Number of 1 Bits <span style="color:green">Easy</span>

## **The Problem**
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

## **Examples**
**Example 1**
```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```
**Example 2**
```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```
**Example 3**
```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

## **The Solution**
This method removes the rightmost binary while incrementing a count. The end result is we return the counter.
What happens binary wise is we decrease the binary number by one and then use *&* to use a bitwise operation *and* (each bits of the output is 1 if the corresponding bit of X AND of Y is 1, otherwise it's 0). 
```
n = 10110100
10110011 = n - 1
n & (n-1)
 10110100
-10110011
----------
 10110000

10101111 = n - 1
n & (n-1)
 10110000
-10101111
----------
 10100000
```
As we loop through the while loop, we increment the counter by 1 as we are removing all the 1's.

## **The Code**

```python
def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
```