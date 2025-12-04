class Solution:
    def countCollisions(self, dirs: str) -> int:
        dirs = dirs.lstrip('L')
        dirs = dirs.rstrip('R')
        return (len(dirs)- dirs.count('S'))