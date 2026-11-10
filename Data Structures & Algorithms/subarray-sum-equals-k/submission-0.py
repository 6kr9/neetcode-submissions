class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum = ans = 0
        prefix = defaultdict(int)
        prefix[0] = 1 

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            ans += prefix[diff]
            prefix[curr_sum] += 1

        return ans    




        