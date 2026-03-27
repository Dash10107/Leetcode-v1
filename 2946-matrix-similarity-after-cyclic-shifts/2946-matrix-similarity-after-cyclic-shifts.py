class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        new = []
        k %= n
        for i,row in enumerate(mat):
            if i&1:
                new.append(row[-k:]+row[:-k])
            else:
                new.append(row[k:]+row[:k])
        return new==mat