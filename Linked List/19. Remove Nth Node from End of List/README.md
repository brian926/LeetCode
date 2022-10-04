# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) <span style="color:orange">Medium</span>

## **The Problem**
Given the *head* of a linked list, remove the *nth* node from the end of the list and return its head.

## **Examples**
**Example 1**

![exampleImg](remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2**
```
Input: head = [1], n = 1
Output: []
```

**Example 2**
```
Input: head = [1,2], n = 1
Output: [1]
```

## **The Solution**
NeetCode uses a dummy in their solution, but below we'll use the same methodology except without using a dummy ListNode.
The concept is we have our two pointers, left and right, which right will be the end of the list and left will be N numbers away from right. To start, we'll move our right pointer N numbers through the list so we now know left is N away from right since they both started at head. We check if the N is outside the range and return the next from head. Now, while there is still a right.next we will move our left and right pointers through the list until right pointer is at the end. Since right pointer is the end and we know the left.next is our target, we'll then point left.next to the next.next node instead which pushed our targeted node out. Lastly, return the head.

## **The Code**

```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    left = right = head
    
    for _ in range(n):
        right = right.next
        
    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next
        
    left.next = left.next.next
    
    return head
```