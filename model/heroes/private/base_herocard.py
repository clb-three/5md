class BaseHeroCard():
    def play(self):
        raise Exception('Not implemented')

    @staticmethod
    def all():
        raise Exception('Not implemented')

    def __eq__(self, other):
        return self.__str__() == other.__str__()
