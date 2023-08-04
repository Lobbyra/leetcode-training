from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if i + j == target:
                    print([i, j])
                    return [i, j]

s = Solution()

print(s.twoSum([2,7,11,15], 9))
