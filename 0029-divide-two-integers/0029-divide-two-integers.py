class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        negative = False
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        if (dividend < 0) != (divisor < 0):
            negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            previous = divisor
            tracker = 1
            while previous + previous <= dividend:
                previous = previous + previous
                tracker = tracker + tracker

            answer += tracker
            dividend -= previous

        if negative == True:
           answer = -abs(answer)

        return answer
