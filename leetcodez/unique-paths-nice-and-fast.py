from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        comb = 1
        for x in range(n, m + n - 1):
            comb *= x
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


print(Solution().uniquePaths(5, 5))
