class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = {}
        self.unrented = defaultdict(SortedSet)
        self.rented = SortedSet()
        for s,m,p in entries:
            self.unrented[m].add((p,s))
            self.prices[(s,m)]=p


    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented:return []
        res = []
        for p,s in self.unrented[movie]:
            res.append(s)
            if len(res)==5:break
        return res
        
    def rent(self, shop: int, movie: int) -> None:
        p = self.prices[(shop,movie)]
        self.unrented[movie].remove((p,shop))
        self.rented.add((p,shop,movie))


    def drop(self, shop: int, movie: int) -> None:
        p = self.prices[(shop,movie)]
        self.rented.remove((p,shop,movie))
        self.unrented[movie].add((p,shop))
        

    def report(self) -> List[List[int]]:
        res = []
        for p,s,m in self.rented:
            res.append([s,m])
            if len(res)==5:break
        return res
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()