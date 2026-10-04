class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = ""
        longest = 0
        for i in range(len(s)):
            if s[i] in answer:
                if longest <= len(answer):
                    longest = len(answer)
                index = answer.find(s[i])
                answer = answer[index + 1::]
                answer += s[i]
            else:
                answer += s[i]
        if longest <= len(answer):
            longest = len(answer)
        return longest