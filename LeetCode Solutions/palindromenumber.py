class Solution:
    def isPalindromeSTR(self, x: int) -> bool:
        reversed = str(x)[::-1]

        return str(x) == reversed

    def isPalindrome(selfself, x: int) -> bool:

        if x < 0:
            return False

        original = x
        reversed = 0

        while x > 0:
            digit = x % 10
            reversed = reversed * 10 + digit
            x = x // 10


        return original == reversed


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindromeSTR(121))
    print(sol.isPalindromeSTR(122))
    print(sol.isPalindromeSTR(123454321))
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(122))
    print(sol.isPalindrome(123454321))