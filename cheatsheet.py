## the "main" file hack

if __name__ == "__main__":
    ## string interpolation
    print(f"hello, my __name__ is {__name__}")

## no newline
print("start line", end="")
print("... end of same line")


## Collections

## Tuple
def int_div(x: int, y: int) -> tuple[int, int]:
    # // - integer division
    return x // y, x % y


a, b = int_div(11, 4)

## List
l0: list[int] = list()
l1: list[int] = list(range(1, 10))

# negative) indexing and step
print(f"slice l1[from_incl:to_incl:step] = {l1[1:-1]}")

## decorators

from typing import Any, TypeVar, Callable

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def debug(f: Callable[[Any], T2]) -> Callable[[Any], T2]:
    def f_debug(*args: Any, **kwargs: Any) -> T2:
        print(f"before: {f.__name__}({args}{kwargs})")
        result: T2 = f(*args, **kwargs)
        print(f"after: {f.__name__}({args}{kwargs}): {result}")
        return result

    return f_debug


# def compose(f, g):
#     def _composed(*args, **kwargs):
#         return g(f(*args, **kwargs))

#     return _composed


# @debug
# def inch_to_foot(x):
#     return x / 12


# @debug
# def foot_to_meter(x):
#     return x * 0.3048


# inch_to_foot_to_meter = compose(inch_to_foot, foot_to_meter)
# # print(inch_to_foot_to_meter(12))


# def partial(f, *f_args, **f_keywords):
#     def g(*args, **kwargs):
#         keywords = f_keywords.copy()
#         keywords.update(kwargs)
#         return f(*(f_args + args), **keywords)

#     return g


# func = lambda x, y, z: x**2 + 2 * y + z
# pfunc = partial(func, 1)
# # print(pfunc(3, 4))  # Output is 8


# def curry(f):
#     argc = f.__code__.co_argcount
#     f_args = []
#     f_kwargs = {}

#     def g(*args, **kwargs):
#         nonlocal f_args, f_kwargs
#         f_args += args
#         f_kwargs.update(kwargs)
#         if len(f_args) + len(f_kwargs) == argc:
#             return f(*f_args, **f_kwargs)
#         else:
#             return g

#     return g


# cfunc = curry(func)
# # print(cfunc(1)(2)(1))


# def trace(f):
#     level = 1

#     def helper(*arg):
#         nonlocal level
#         print(
#             (level - 1) * "  │",
#             "  ┌",
#             f.__name__,
#             "(",
#             ",".join(map(str, arg)),
#             ")",
#             sep="",
#         )
#         level += 1
#         result = f(*arg)
#         level -= 1
#         print((level - 1) * "  │", "  └", result, sep="")
#         return result

#     return helper


# def memoize(f):
#     memo = {}

#     def memoized(x):
#         if x not in memo:
#             memo[x] = f(x)
#         return memo[x]

#     return memoized


# @trace
# @memoize
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# # fib = trace(fib)

# fib(5)
# fib(6)
