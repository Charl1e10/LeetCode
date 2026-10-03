class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            rx = str(x)[::-1]
        else:
            rx = str(x)[:0:-1]
            rx = "-" + rx
        
        if int(rx) < -2147483648 or int(rx) > 2147483647:
            return 0

        return int(rx)
        
        