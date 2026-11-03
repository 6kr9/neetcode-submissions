class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 0
        right = max(piles)

        def func(mid : int, piles) ->int:
            hr = 0
            print(f"{mid} ")

            for i in piles:
                if i<= mid:
                    hr += 1
                else:
                    if i%mid == 0:
                        hr += i//mid
                    else:
                        hr = hr + i//mid + 1

            return hr
        
        while left < right:

            mid = (left + right)//2
            if mid == 0:
                return 1

            if func(mid, piles) <= h:
                right = mid
            else:
                left = mid + 1

        return left
        