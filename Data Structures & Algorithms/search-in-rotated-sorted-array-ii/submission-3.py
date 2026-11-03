class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if len(nums) == 1 or (min(nums) == max(nums)):
            return nums[0] == target

        l1 = 0
        r2 = len(nums) -1
        flag = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                r1 = i-1
                l2 = i
                flag = True
                break

        def func(left, right)->bool:

            while left<right:
                mid = (left+right)//2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid+1

            if left == right and nums[right] == target:
                return True

            return False

        if flag == False:
            return func(l1,r2)


        return func(l1, r1) or func(l2, r2)
            
        