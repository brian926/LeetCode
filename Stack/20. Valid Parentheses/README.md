# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) <span style="color:green">Easy</span>

## **The Problem**
Given a string *s* containing just the characters *'('*, *')'*, *'{'*, *'}'*, *'['* and *']'*, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## **Examples**
**Example 1**
```
Input: s = "()"
Output: true
```
**Example 2**
```
Input: s = "()[]{}"
Output: true
```

**Example 3**
```
Input: s = "(]"
Output: false
```

## **The Solution**
First we'll create a stack with closing cases. We know that if the string starts with a closing case, then it is fasle because it'll never be able to close. We then create an array and set through the string provided. If that character isn't in the map (that it isn't a closing case) then we append it onto the list and continue. However, if that is not the case we then check if the list is not empty or if the last character in the list is not a corresponding opening case. Meaning, we will return false for (]. If we pass both those if statements, that means the last character of the array is a opening case and this current string is the closing case so we just pop off the last character of the list (the opening case). This way cases such as ([{}]) are still true.

## **The Code**

```python
    def isValid(self, s: str) -> bool:
        Map = { ")" : "(", "}" : "{", "]" : "[" }
        
        arr = []
        for c in s:
            if c not in Map:
                arr.append(c)
                continue
            if not arr or arr[-1] != Map[c]:
                return False

            arr.pop()
       
        return not arr
```