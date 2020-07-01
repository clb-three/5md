

class Dictable:
    def __iter__(self):
        blacklist = ['script', 'notifier', 'mutex', 'event_task']

        # first start by grabbing the Class items
        iters = dict((k, v) for k, v in self.__dict__.items()
                     if k not in blacklist and not k.startswith('__'))

        # then update the class items with the instance items
        iters.update(self.__dict__)

        # now 'yield' through the items
        for key, val in iters.items():
            if key not in blacklist:
                yield key, val
