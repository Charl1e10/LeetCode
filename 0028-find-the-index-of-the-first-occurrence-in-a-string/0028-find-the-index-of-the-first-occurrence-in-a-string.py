class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(i ,len(haystack) + 1):
                if haystack[i:j] == needle:
                    return i
        
        else:
            return -1