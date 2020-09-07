from collections import Counter
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def cnt_triple(cnt1, cnt2):
            cnt = 0
            for v in cnt1:
                vs = v * v
                for j in cnt2:
                    if vs % j == 0:
                        rj = vs // j 
                        if rj not in cnt2 or rj > j:
                            continue
                        c1 = cnt2[j]
                        c2 = cnt2[rj] - (j==rj)
                        cnt += (c1 * c2 ) * cnt1[v] // (2 if j == rj else 1)
                        # print(v, j, rj, cnt1[v], c1, c2, cnt)
            return cnt

                    
        s1 = Counter(nums1)
        s2 = Counter(nums2)
        return cnt_triple(s1, s2) + cnt_triple(s2, s1)
        
