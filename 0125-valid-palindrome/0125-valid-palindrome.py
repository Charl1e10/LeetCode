class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        
        reverse = clean[::-1]

        if reverse == clean:
            return True
        else:
            return False

        