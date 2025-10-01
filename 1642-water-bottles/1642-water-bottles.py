class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        init = numBottles
        while numBottles>=numExchange:
            numBottles-=(numExchange-1)
            init+=1
        return init
        
