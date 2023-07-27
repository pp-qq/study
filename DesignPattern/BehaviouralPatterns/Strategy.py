from abc import ABC, abstractmethod


class FilterStrategy(ABC):
    @abstractmethod
    def removeValue(self, value):
        pass


class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, value):
        return value >= 0


class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, value):
        return value % 2 == 0


class Values:
    def __init__(self, values):
        self.values = values

    def filter(self, strategy):
        result = []
        for value in self.values:
            if strategy.removeValue(value):
                result.append(value)
        return result


values = Values([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

print(values.filter(RemoveNegativeStrategy()))  # [1, 2, 3, 4, 5]
print(values.filter(RemoveOddStrategy()))  # [2, 4, -2, -4]
