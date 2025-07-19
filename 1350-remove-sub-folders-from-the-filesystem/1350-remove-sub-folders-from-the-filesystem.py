class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        arr = []
        folder.sort()
        for f in folder:
            if not arr or not f.startswith(arr[-1]+'/'):
                arr.append(f)
        return arr