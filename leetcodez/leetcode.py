@lru_cache(maxsize=100000)
def uniquePathsMemo(m, n):
    if n == 1 or m == 1:
        return 1
    return uniquePathsMemo(m - 1, n) + uniquePathsMemo(m, n - 1)


def fac(frm, to):
    r = 1
    for x in range(frm, to + 1):
        r = r * x
    return r


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return fac(m, m + n - 2) // fac(1, n - 1)
