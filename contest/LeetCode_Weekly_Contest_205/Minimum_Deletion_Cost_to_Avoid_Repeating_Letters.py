from collections import defaultdict
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        prev = ''
        maxv = 0
        ttlv = 0
        rst = 0
        for i, v in enumerate(s):
            c = cost[i]
            if v != prev:
                rst += ttlv - maxv 
                maxv = c
                ttlv = c
                prev = v
            else:
                maxv = max(maxv, c)
                ttlv += c
        return rst + ttlv - maxv

