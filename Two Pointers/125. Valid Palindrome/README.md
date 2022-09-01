# 125. Valid Palindrome

## **The Problem**
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string *s*, return *true* if it is a **palindrome**, or *false* otherwise.

### **Examples**
Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
**Example 3:**
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## **The Solution**

To handle this problem, we will use two pointers (one on the left more character and one all the right most). Then compare the two characters, since a palindrome is the same forwards and back then moving the two pointers through the string should be equal;
```
"A man, a plan, a canal: Panama"
[A] man, a plan, a canal: Panam[a]
A [m]an, a plan, a canal: Pana[m]a
A m[a]n, a plan, a canal: Pan[a]ma
```
Since we are removing all non-alphanumeric characters, we won't have to worry about empty spaces or special characters.

For the code, we first define a function that inputs a character and returns true or false if there is a unicode code of that character.
Then we initialize our pointers, our left pointer at 0 and right pointer at the end of the string. After while the left pointer is less than the right pointer, we first if there is a non-alphanumeric character. If there is, we move the pointers by one else we check if the two characters are not equal. When this occurs we return false otherwise we move both pointers up.

## **The Code**

```python
def isPalindrome(self, s: str) -> bool:
        def aplhaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
        
        l, r = 0, len(s) -1
        while l < r:
            while l < r and not aplhaNum(s[l]):
                l += 1
            while  l < r and not aplhaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l +1, r -1
        return True
```