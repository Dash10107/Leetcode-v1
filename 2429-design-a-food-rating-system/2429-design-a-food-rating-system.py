class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ftoc = {};self.ftor={};self.ctoheap={}
        for f,c,r in zip(foods,cuisines,ratings):
            self.ftoc[f]=c
            self.ftor[f]=r
            if c not in self.ctoheap:
                self.ctoheap[c]=[]
            heappush(self.ctoheap[c],(-r,f))

        

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.ftoc[food]
        self.ftor[food]=newRating
        heappush(self.ctoheap[c],(-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.ctoheap[cuisine]
        while heap:
            r,f = heap[0]
            if -r == self.ftor[f]:
                return f
            heappop(heap)

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)