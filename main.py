#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: main.py
# @time: 2019-12-21 18:41
# @desc:

import re
import os
import math


class LanguageModelContent:

    def __init__(self, possibility, words, punishment):
        self.possibility = possibility
        self.words = words
        self.punishment = punishment

    def __str__(self):
        return self.possibility + '\t' + self.words + '\t' + self.punishment


def write_language_1model(unary_model, binary_class_count, unary_count):
    with open('output.txt', 'a') as file:
        file.write('ngram 2=' + str(binary_class_count) + '\n')
        file.write('\n')
        file.write('\\1-grams:\n')
    # count 1 length word and n length word, n>1
    unary_model_keys = unary_model.keys()
    language_1models = []
    for key in unary_model_keys:
        count = unary_model.get(key)
        conditional_possibility = math.log10(count / unary_count)
        conditional_possibility = round(conditional_possibility, 6)
        model1 = LanguageModelContent(str(conditional_possibility), key, str(-99))
        language_1models.append(model1)
    with open('output.txt', 'a') as file:
        for model in language_1models:
            file.write(str(model) + '\n')

        file.write('\n')
        file.write('\\2-grams:\n')


if __name__ == "__main__":

    with open('output.txt', 'a') as file:
        file.write('\data\\\n')

    unary_model = {}

    unary_class_count = 0
    unary_count = 0
    with open('/Users/geekye/Documents/Dataset/LM/UniBiGram/ngrams-00000-of-00394') as file:
        for line in file:
            if re.match('^[\u4e00-\u9fa5]{1,}', line) and line != '' and line != '\n':
                content = line.split('\t')
                key = content[0]
                value = int(content[1])
                unary_count = unary_count + value
                unary_class_count = unary_class_count + 1
                unary_model[key] = value

    with open('output.txt', 'a') as file:
        file.write('ngram 1=' + str(unary_class_count) + '\n')

    binary_class_count = 0
    files = os.listdir('/Users/geekye/Documents/Dataset/LM/UniBiGram')

    files_valid = [file for file in files if file != 'ngrams-00000-of-00394']

    language_1model_switch = True
    for binary_file in files_valid:

        language_models = []
        with open('/Users/geekye/Documents/Dataset/LM/UniBiGram/' + binary_file) as file:
            for line in file:
                if re.match('^[\u4e00-\u9fa5]{1,}', line) and line != '' and line != '\n':
                    content = re.split('[\s\t]+', line)
                    under_word = content[0]
                    after_word = content[1]
                    if re.match('^[\u4e00-\u9fa5]{1,}', after_word):
                        words = under_word + ' ' + after_word
                        union_count = int(content[2])
                        binary_class_count = binary_class_count + 1
                        count = unary_model.get(under_word)
                        if count is not None:
                            conditional_possibility = union_count / count
                            conditional_possibility = math.log10(conditional_possibility)
                            conditional_possibility = round(conditional_possibility, 6)
                            language_model = LanguageModelContent(str(conditional_possibility), words, str(-99))
                            language_models.append(language_model)

            # this process can run in first loop
            if language_1model_switch:
                write_language_1model(unary_model, binary_class_count, unary_count)
                language_1model_switch = False

        with open('output.txt', 'a') as file:
            for model in language_models:
                file.write(str(model) + '\n')

    with open('output.txt', 'a') as file:
        file.write('\\end\\')
        file.write('ngram 2=' + str(binary_class_count) + '\n')