#!/usr/bin/env python3

import re

class MyString():

    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            print(f"Setting value to {value}")
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if self.value == '':
            return 0
        else:
           
            sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self.value) if sentence.strip()]
            return len(sentences)


