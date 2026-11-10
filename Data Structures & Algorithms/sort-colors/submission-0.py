class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = [0]*3

        for num in nums:
            if num == 0:
                temp[0] += 1
            elif num == 1:
                temp[1] += 1
            else:
                temp[2] += 1

        nums.clear()  
        val = 0      

        for i in temp:
            for j in range(0,i):
                nums.append(val)

            val += 1

        return         

        