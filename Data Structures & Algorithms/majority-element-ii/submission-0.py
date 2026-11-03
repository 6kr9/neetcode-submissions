class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        k = n/3
        dic = defaultdict(int)
        ans = set()

        for i in nums:
            dic[i] += 1
            if dic[i] > k:
                ans.add(i)

        return list(ans)
        