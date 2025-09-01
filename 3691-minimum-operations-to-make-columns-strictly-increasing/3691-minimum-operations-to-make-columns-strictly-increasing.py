class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid);n=len(grid[0])
        lista=[]
        cost=0
        for i in range (0,n):
            for j in range(0,m):
                lista.append(grid[j][i])
            length=len(lista)
            for k in range (1,length):
                if lista[k]<=lista[k-1]:
                    cost+= lista[k-1]-lista[k]+1
                    lista[k]=lista[k-1]+1
            lista=[]
        return  cost
        