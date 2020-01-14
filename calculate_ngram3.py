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

if __name__ == "__main__":
    with open('ngram3.txt','a') as file:
        file.write('\\3-grams:')

    dir_list = sorted(os.listdir('/home/fourier/Data/data'))

    grams_2_dir = sorted(os.listdir('/home/fourier/Data/processed_file/data/unfilter_data/ngram2')) 

    # because ngrams-[00030 - 00036]-of-00394 have no invalid  data
    filtered_list = [dir for dir in dir_list if dir >= 'ngrams-00037-of-00394' and dir <= 'ngrams-00132-of-00394']

    conditonal_2count=0
    for file in filtered_list:
        with open('/home/fourier/Data/data/'+file) as file:
            for line in file:
                if re.match('^[\u4e00-\u9fa5]{1,8}[\s\t][\u4e00-\u9fa5]{1,8}[\s\t][\u4e00-\u9fa5]{1,8}[\s\t]\d{1,}',line):
                    segments = re.split('[\s\t]+]',line)
                    first_word = segments[0]
                    second_word = segments[1]
                    third_word = segments[2]
                    words_count = segments[3]

                    grams_2 = first_word + ' '+ second_word

                    if conditonal_2count =0:
                        for file in grams_2_dir:
                            with open('/home/fourier/Data/processed_file/data/unfilter_data/ngram2/'+file) as file:
                                for line in file:
                                    segments = line.split('\t')
                                    # todo                                    




