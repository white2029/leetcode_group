class Solution:
    def modifyString(self, s: str) -> str:
        prev = ''
        rst = ''
        chars = 'abcdefghijklkmoprqstuvwxyz'
        for i in range(0, len(s)):
            sc = s[i]
            if s[i] == '?':
                last = '' if i+1 >= len(s) else s[i+1]
                for v in chars:
                    if v != prev and v != last:
                        sc = v
                        break
            rst += sc
            prev = sc
        return rst
