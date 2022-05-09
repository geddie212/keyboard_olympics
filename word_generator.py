from random import choice


class WordGenerator:

    def __init__(self):
        from word_list import common_word_list
        self.common_words = common_word_list

    def generate_words(self, quantity):
        word_list = []
        for i in range(0, quantity):
            word_list.append(choice(self.common_words).lower() + ' ')

        return ''.join(word_list)
