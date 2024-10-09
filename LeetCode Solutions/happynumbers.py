class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1

    def start(self):
        print(self.isHappy(19))
        print(self.isHappy(2))
        print(self.isHappy(7))
        print(self.isHappy(91))

if __name__ == '__main__':
    sol = Solution()
    sol.start()