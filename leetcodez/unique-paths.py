# from functools import lru_cache
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper2(m: int, n: int, cache: List[List[int]]) -> int:
            if m == 0 or n == 0:
                return 0
            if m == 1 or n == 1:
                return 1
            else:
                if cache[m][n] != -1:
                    return cache[m][n]
                elif cache[n][m] != -1:
                    return cache[n][m]
                else:
                    partial_sum = helper2(m - 1, n, cache) + helper2(m, n - 1, cache)
                    cache[m][n] = partial_sum
                    cache[n][m] = partial_sum
                    return partial_sum

        maxn = max(m, n)
        # cache = [[-1] * (maxn + 1)] * (maxn + 1)
        cache = [[-1] * (maxn + 1) for i in range(maxn + 1)]
        # print(f"Cache: {len(cache)}x{len(cache[0])}")
        return helper2(m, n, cache)


print(Solution().uniquePaths(4, 4))
