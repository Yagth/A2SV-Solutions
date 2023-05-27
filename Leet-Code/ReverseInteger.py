class Solution:
    def reverse(self, x: int) -> int:
        sign = 1

        if x < 0:
            sign = -1

        s = str(abs(x))
        sr = s[::-1]

        xr = sign * int(sr)

        if xr > pow(2, 31) or xr < (-1 * pow(2, 31)):
            return 0

        return xr
