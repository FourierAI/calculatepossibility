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

if __name__ == "__main__":

    gram_2 = {}
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count.out', encoding='utf-8') as file:
        for line in file:
            try:
                segments = re.split('[\t\s]+',line)
                first_word = segments[0]
                second_word = segments[1]
                count = segments[2]
                gram_2[first_word + ' '+second_word] = count
            except Exception as ex:
                traceback.print_exc()
                print(line)
                print('segment[0]：',segments[0])
                print('segment[1]：',segments[1])
                print('segment[2]：',segments[2])
                
    print(gram_2.get('一 一'))