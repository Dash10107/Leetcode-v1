class Solution:
    def checkSubarraySum(self, arr: List[int], k: int) -> bool:
        mod_map = {0: -1}
        t = 0
        for i,n in enumerate(arr):
            t+=n
            rem = t%k if k!=0 else t
            if rem in mod_map:
                if i-mod_map[rem]>=2:
                    return True
            else:
                mod_map[rem]=i
        return False