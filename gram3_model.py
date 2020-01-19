#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: calculate_ngram3.py
# @time: 2020-01-14 01:27
# @desc:

import codecs
import math
import os
import re
import sys
import traceback

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


class LanguageModelContent:

    def __init__(self, possibility, words, punishment=''):
        self.possibility = possibility
        self.words = words
        self.punishment = punishment

    def __str__(self):
        return str(self.possibility) + '\t' + self.words + '\t' + self.punishment


if __name__ == "__main__":

    ngram2 = {}
    dir = sorted(os.listdir('/Data_SSD/zhipengye/zhipengye/LM/processed_data/small_full_chinese_filtered'))

    ngram2_files = [file_name for file_name in dir if file_name>= 'ngrams-00001-of-00394' and file_name <= 'ngrams-00029-of-00394']
    ngram3_files = [file_name for file_name in dir if file_name>= 'ngrams-00030-of-00394' and file_name <= 'ngrams-00132-of-00394']

    for file_name in ngram2_files:
        with open('/Data_SSD/zhipengye/zhipengye/LM/processed_data/small_full_chinese_filtered/'+file_name,encoding='utf-8') as file:
            for line in file:
                segments = line.split('\t')
                words = segments[0].replace(' ','')
                count = float(segments[1])
                ngram2[words] = count

    for file_name in ngram3_files:
        model_list = []
        with open('/Data_SSD/zhipengye/zhipengye/LM/processed_data/small_full_chinese_filtered/'+file_name,encoding='utf-8') as file:
            for line in file:
                segments = line.split('\t')
                count = float(segments[1])
                words = segments[0].split(' ')
                first_word = words[0]
                second_word = words[1]
                third_word = words[2]
                gram2_count = ngram2.get(first_word+second_word)
                if gram2_count is not None:
                    possibility = math.log10(count/gram2_count)
                    words = segments[0]
                    model = LanguageModelContent(possibility, segments[0])
                    model_list.append(model)
        with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/gram3/'+file_name, 'a',encoding='utf-8') as file:
            for model in model_list:
                file.write(str(model) + '\n')