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

    gram_2 = {}
    with open('/Data_HDD/zhipengye/data/gram2/gram2_count.out') as file:
        for line in file:
            segments = line.split('\t')
            words = segments[0]
            count = segments[1]
            gram_2[words] = count
    
    print(gram_2.get('一 一'))




