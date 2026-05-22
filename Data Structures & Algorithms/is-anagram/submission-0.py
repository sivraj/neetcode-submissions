class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        chrs = {}
        for i in range(len(s)):
            chrs[s[i]] = chrs.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] not in chrs:
                return False
            chrs[t[i]] = chrs[t[i]] -1

            if chrs[t[i]] < 0:
                return False
        return True
            