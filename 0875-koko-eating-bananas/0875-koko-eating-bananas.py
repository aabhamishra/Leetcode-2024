import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if eating n bananas per hour, ceil(piles[i]/n) for all = h
        # min speed = 1 banana per hour
        # max speed = largest pile per hour
        
        min = 1
        max = 1
        for pile in piles:
            max = pile if pile > max else max
        
        while min < max:
            if min == max:
                return min
            
            mid = (max + min)//2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
                        
            if time > h:
                min = mid + 1
            else:
                max = mid

        return min
                



