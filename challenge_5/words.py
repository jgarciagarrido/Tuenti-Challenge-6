from operator import itemgetter
import re

class WordDictionary():
    def __init__(self, filename):
        f = open(filename)
        lines = f.readlines()
        self.words = map(lambda x: x.rstrip("\r\n"), lines)


class WordSeeker():
    def __init__(self, words):
        self.words = words
        self.letters_used = []
        self.candidates = words[:]

    def select_by_regex(self, expresion):
        print expresion
        filter = re.compile("^" + expresion + "$")
        self.candidates = [word for word in self.candidates if filter.match(word)]

    def add_used_letter(self, letter):
        self.letters_used.append(letter)

    def get_letter(self):
        letters = LetterCounter(self.candidates)
        letters.most_frequent_letters()
        for ocurrence in letters.ocurrences_ordered:
            if ocurrence[0] not in self.letters_used:
                self.add_used_letter(ocurrence[0])
                return ocurrence[0]
        return " "

    def reset(self):
        self.letters_used = []
        self.candidates = self.words[:]

class LetterCounter():
    def __init__(self, words):
        self.words = words
        self.ocurrences = {}
        self.ocurrences_ordered = []

    def count(self):
        for word in self.words:
            for letter in list(word):
                if letter in self.ocurrences:
                    self.ocurrences[letter] += 1
                else:
                    self.ocurrences[letter] = 1

    def most_frequent_letters(self):
        self.count()
        self.ocurrences_ordered = self.ocurrences.items()
        self.ocurrences_ordered = sorted(self.ocurrences_ordered, key=itemgetter(1), reverse=True)
