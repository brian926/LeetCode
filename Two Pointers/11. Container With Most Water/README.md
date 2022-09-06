# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) <span style="color:orange">Medium</span>

## **The Problem**
You are given an integer array *height* of length *n*. There are *n* vertical lines drawn such that the two endpoints of the *ith* line are *(i, 0)* and *(i, height[i])*.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

*Return the maximum amount of water a container can store.*

## **Examples**
**Example 1**

![exampleImg](img.jpg)
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```
**Example 2**
```
Input: height = [1,1]
Output: 1
```

## **The Solution**
[sgallivan](https://leetcode.com/problems/container-with-most-water/discuss/1069746/JS-Python-Java-C%2B%2B-or-2-Pointer-Solution-w-Visual-Explanation-or-beats-100) gives a great explanation on how to use 2 pointers in multiple languages on LeetCode.
The amount of water will also be a rectange so the area would be length * width, with width being the difference between the index of the two lines (i and j) and hieght the lowest of those two lines. For this, we'll start with opposite sides and move inwards checking if the area is larger which would only be possible if height increased.
The first thing is to set answer to 0 and then the left and right pointers. While the pointers aren't equal we check if the left pointer is small than right which if it is, our value will be the height of the smaller line times our width (which is the right pointer minus how far left we are). Then we increase our left pointer by one and check if our value is greater than our answer and if it is we pass it to our answer. If the left pointer line is greater than the right pointer, we do the same but use our right pointer since it is the smaller value.

## **The Code**

```python
def maxArea(self, H: List[int]) -> int:
        ans, i, j = 0, 0, len(H)-1
        while (i < j):
            if H[i] <= H[j]:
                res = H[i] * (j - i)
                i += 1
            else:
                res = H[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans
```