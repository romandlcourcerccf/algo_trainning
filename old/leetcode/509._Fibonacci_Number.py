class Solution:
    def fib(self, n: int) -> int:
        def cached(f):
            cache = {}

            def worker(*args):
                if args not in cache:
                    cache[args] = f(*args)
                return cache[args]

            return worker

        @cached
        def _fib(n):
            if n <= 1:
                return n
            else:
                return _fib(n - 1) + _fib(n - 2)

        return _fib(n)


from functools import lru_cache


class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def _fib(n):
            if n <= 1:
                return n
            else:
                return _fib(n - 1) + _fib(n - 2)

        return _fib(n)
