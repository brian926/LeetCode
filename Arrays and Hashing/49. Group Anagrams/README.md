# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) <span style="color:orange">Medium</span>

## **The Problem**
Given an array of strings *strs*, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## **Examples**
**Example 1**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**
```
Input: strs = [""]
Output: [[""]]
```
**Example 3**
```
Input: strs = ["a"]
Output: [["a"]]
```

## **The Solution**
Our method of solve this is to create a default dictonary which we can add use our strings as sorted keys and then append that string to the respected keys. For example, "tea" which would be hashmap[aet] which we can then append "eat", "tea", and "ate" as all those values sorted would be "aet". 
We first declare our default dictonary, which allows us to have multiple values per key, then we step though the array of strings. For each string sorted as our key, we append that string and finally after the loop we return the values of the default dictonary.

## **The Code**
### Python

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[str(sorted(s))].append(s)
        return hashmap.values()
```
### JavaScript
```JavaScript
var groupAnagrams = function(strs) {
    let map = {}
    
    for (let x of strs) {
        let key = [...x].sort()
        map[key] = map[key] ? [...map[key], x] : [x]
    }
    
    return Object.values(map)
};
```