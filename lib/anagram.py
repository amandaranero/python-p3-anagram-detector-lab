
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        list = [el for el in list if sorted(self.word)== sorted(el)]
        return list






# [el for el in list if sorted(word)== sorted(el)]
        

    





