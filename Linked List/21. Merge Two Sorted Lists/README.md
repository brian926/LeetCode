# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) <span style="color:green">Easy</span>

## **The Problem**
You are given the heads of two sorted linked lists *list1* and *list2*.
Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.
*Return the head of the merged linked list*.

## **Examples**
**Example 1**

![exampleImg](merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 2**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## **The Solution**
We'll create our new list as our first step and then we pass through the list. While we have both lists, if one value is less than the other we'll add it as the next node in our list and then get the next value in its own list. Then, get the next value in our new list and continue until one list is completed. Lastly, if there is anything left in either list then we'll append it onto the end of our new list.

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