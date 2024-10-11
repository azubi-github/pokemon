

class Ability:


    def __init__(self, name, Attack_Strength, Accuracy, element):
        self.__name = name
        self.__attack_strength = Attack_Strength
        self.__accuracy = Accuracy
        self.__element = element

    def get_name(self):
        return self.__name
    def get_attack_strength(self):
        return self.__attack_strength
    def get_accuracy(self):
        return self.__accuracy
    def get_element(self):
        return self.__element