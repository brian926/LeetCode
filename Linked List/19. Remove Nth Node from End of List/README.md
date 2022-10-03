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


## **The Code**

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
    newlist = ListNode(0)
    arr = newlist
    while list1 and list2:
        if list1.val < list2.val:
            arr.next = list1
            list1 = list1.next
        else:
            arr.next = list2
            list2 = list2.next
        arr = arr.next

    arr.next = list1 or list2
    return newlist.next
```