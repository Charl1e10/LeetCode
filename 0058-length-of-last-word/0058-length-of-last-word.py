class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.split()
        return len(ss[len(ss) - 1])