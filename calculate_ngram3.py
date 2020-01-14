#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: calculate_ngram3.py
# @time: 2020-01-14 01:27
# @desc:

import os
import re
import main
import math
import traceback
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


class LanguageModelContent:

    def __init__(self, possibility, words, punishment=''):
        self.possibility = possibility
        self.words = words
        self.punishment = punishment

    def __str__(self):
        return self.possibility + '\t' + self.words + '\t' + self.punishment

if __name__ == "__main__":

    gram_2 = {}
    # with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count', encoding='utf-8') as file:
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2ngrams-00002-of-00394', encoding='utf-8') as file:
        for line in file:
            if '\n' is not line and '' is not line: 
                try:
                    segments = re.split('[\t\s]+',line)
                    first_word = segments[0]
                    second_word = segments[1]
                    count = segments[2]
                    gram_2[first_word + ' '+second_word] = count
                except Exception as ex:
                    traceback.print_exc()
                    print('line is :',line)
                    
    dir_list = os.listdir('/Data_SSD/zhipengye/zhipengye/data/original_data/Data/data')

    # because ngrams-[00030 - 00036]-of-00394 have no invalid  data
    # filtered_list = [dir for dir in dir_list if dir >= 'ngrams-00037-of-00394' and dir <= 'ngrams-00132-of-00394']
    filtered_list = [dir for dir in dir_list if dir >= 'ngrams-00037-of-00394' and dir <= 'ngrams-00038-of-00394']


    model_list = []
    for file_name in filtered_list:
        with open('/Data_SSD/zhipengye/zhipengye/data/original_data/Data/data/'+file_name, encoding='utf-8') as file:
            for line in file:
                if re.match('^[\u4e00-\u9fa5]{1,8}[\s\t]{1,}[\u4e00-\u9fa5]{1,8}[\s\t]{1,}[\u4e00-\u9fa5]{1,8}[\s\t]{1,}\d{1,}',line):
                    segments = re.split('[\s\t]+', line)
                    first_word = segments[0]
                    second_word = segments[1]
                    third_word = segments[2]
                    words = first_word+' '+second_word + ' '+third_word
                    count = float(segments[3])

                    gram_2_words = first_word + ' ' +second_word
                    gram_2_count = gram_2.get(gram_2_words)

                    if gram_2_count != None:
                        conditional_possibility = count / float(gram_2_count)
                        conditional_possibility = math.log10(conditional_possibility)
                        conditional_possibility = round(conditional_possibility, 6)
                        model = LanguageModelContent(str(conditional_possibility),words )
                        model_list.append(model)

            if len(model_list) >= 1000000:
                with open('/Data_SSD/zhipengye/zhipengye/data/gram3/gram3','a') as file:
                    for model in model_list:
                        file.write(str(model) + '\n')
                        print('1000000 rows have been processed!')  
                model_list = []

    with open('/Data_SSD/zhipengye/zhipengye/data/gram3/gram3','a') as file:
        for model in model_list:
            file.write(str(model) + '\n')
            print(str(len(model_list))+' rows have been processed!')  