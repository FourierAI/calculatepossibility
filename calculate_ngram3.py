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
import traceback
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
sys.stdout.write("Your content..在.")

if __name__ == "__main__":

    gram_2 = {}
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2ngrams-00002-of-00394', encoding='utf-8') as file:
        for line in file:
            if '' is not line: 
                try:
                    segments = re.split('[\t\s]+'.encode('utf-8'),line)
                    first_word = segments[0]
                    second_word = segments[1]
                    count = segments[2]
                    gram_2[first_word + ' '+second_word] = count
                except Exception as ex:
                    traceback.print_exc()
                    print('line is :',line)
                    
    print(gram_2.get('一 一'))