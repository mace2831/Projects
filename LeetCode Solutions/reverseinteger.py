class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT_32 = 2147483647
        MIN_INT_32 = -2147483648

        reversed = 0
        sign = -1 if x < 0 else 1

        x = abs(x)

        while x > 0:
            digit = x % 10
            reversed = reversed * 10 + digit
            if reversed > MAX_INT_32 or reversed < MIN_INT_32:
                return 0
            else:

                x = x // 10
        reversed *= sign
        return reversed

if __name__ == '__main__':
    #sol = Solution()
    #print(sol.reverse(123))
    #print(sol.reverse(-123))
    #print(sol.reverse(120))
    temp = "24.5M"
    temp1 = temp[-1:]

    print(temp)
    print(temp1)