# [41. Linked list Cycle](https://leetcode.com/problems/linked-list-cycle/) <span style="color:green">Easy</span>

## **The Problem**
Given *head*, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return *true* if there is a cycle in the linked list. Otherwise, return *false*.

## **Examples**
**Example 1**
```mermaid
graph LR
    3 --> 2;
    2 --> 0;
    -4 -- 2;
```
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
**Example 2**
```mermaid
graph LL
    1 --> 2;
    2 --> 1;
```
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```
**Example 3**
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## **The Solution**
This solution uses Flyod's tortoise and hare algorithm, which is a cycle detection problem. This algorithm helps detects if there is a cycle because by using a sequence of iterated function values we must eventually use the same value. With the tortoise and hare algorithm, we use two pointers with one moving twice as fast as the other. Eventually, either we run into the end of the list and it is not a cycle or the pointers are the same value which we then know this is a linked list cycle.
We start both our pointers at the head of the list, then while there is a right pointer and a next in the list we move our values over. If the two values are equal we return true, else we hit the end of the list and break from the while statement and return false.

## **The Code**

```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    left, right = head, head
    
    while right and right.next:
        left = left.next
        right = right.next.next
        if right == left:
            return True
        
    return False
```