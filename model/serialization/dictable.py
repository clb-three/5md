import inspect
import re

builtin_regex = re.compile(r'^__.*__$')


class Dictable:
    def __iter__(self):
        # first start by grabbing the Class items
        iters = inspect.getmembers(self)
        iters = [
            (k, v) for k, v in iters if
            v is not None
            and k != '_abc_impl'
            and k != 'log'
            and not builtin_regex.fullmatch(k)
            and not inspect.ismethod(v)
            and not inspect.isfunction(v)
        ]

        # then update the class items with the instance items

        # now 'yield' through the items
        for key, val in iters:
            yield key, val
