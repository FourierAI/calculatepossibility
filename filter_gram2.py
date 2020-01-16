#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: filter_gram2.py
# @time: 2020-01-16 18:43
# @desc:

import os
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


def verifyContent(words, word_set):
    for word in words:
        if word not in word_set:
            return False
    return True

if __name__ == "__main__":
    word_set =set()
    with open('/Data_SSD/zhipengye/zhipengye/data/filter_rule/WordSegDict.small',encoding='utf-8') as file:
        for line in file:
            word_set.add(line.strip())

    content_list = []
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count',encoding='utf-8') as file:
        for line in file:
            segments = line.split('\t')
            words = segments[0].split(' ')
            flag = verifyContent(words, word_set)
            if flag:
                content_list.append(line.strip())

            if len(content_list) >= 100000:
                with open('/Data_SSD/zhipengye/zhipengye/data/gram2/filtered_gram2_count', 'a', encoding='utf-8') as file:
                    file.write('\n'.join(content_list))
                content_list = []
                print('100000 rows have been processed!')

    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/filtered_gram2_count', 'a',encoding='utf-8') as file:
        file.write('\n'.join(content_list))
