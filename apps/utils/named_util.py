# -*- coding: utf-8 -*-
class NamedTransfer:
    @staticmethod
    def to_camel(word):
        if NamedTransfer.is_under_line(word):
            camel_word = NamedTransfer.underline_to_camel(word)
        else:
            camel_word = word
        return camel_word

    @staticmethod
    def to_under_line(word):
        if NamedTransfer.is_under_line(word):
            under_line_word = word
        else:
            under_line_word = NamedTransfer.camel_to_under_line(word)
        return under_line_word

    @staticmethod
    def underline_to_camel(word):
        word_list = word.split("_")
        camel_list = []
        for i, e in enumerate(word_list):
            if i == 0:
                word = e
            else:
                word = e.capitalize()
            camel_list.append(word)
        return "".join(camel_list)

    @staticmethod
    def camel_to_under_line(word):
        under_line = ""
        for w in word:
            if w.isupper():
                under_line += "_{}".format(w.lower())
            else:
                under_line += w
        return under_line

    @staticmethod
    def is_under_line(word):
        if '_' in word:
            return True
        else:
            return False
