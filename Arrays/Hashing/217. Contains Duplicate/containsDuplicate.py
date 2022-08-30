from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = set()
       
        for i in nums:
            if i in test:
                return True
            else:
                test.add(i)
        return False
