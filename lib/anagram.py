# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Normalize to lowercase

    def match(self, word_list):
        sorted_word = sorted(self.word)  # Sort letters of base word
        return [word for word in word_list if sorted(word.lower()) == sorted_word]

