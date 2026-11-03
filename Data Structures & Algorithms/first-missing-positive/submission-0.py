class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(1,100001):
            if i not in nums:
                return i
        