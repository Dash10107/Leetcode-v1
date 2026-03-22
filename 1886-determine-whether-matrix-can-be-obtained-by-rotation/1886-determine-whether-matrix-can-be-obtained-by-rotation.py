class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rot(m):
            return [list(reversed(col)) for col in zip(*m)]
        mat2 = rot(mat)
        mat3 = rot(mat2)
        mat4 = rot(mat3)

        return (mat==target or mat2==target or mat3==target or mat4==target)