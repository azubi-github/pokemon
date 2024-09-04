class Ability:
    def __init__(self, element, power, accuracy):
        self.__element = element
        self.__power = power
        self.__accuracy = accuracy

    def __repr__(self):
        return f'{self.__element}, {self.__power}, {self.__accuracy}'
