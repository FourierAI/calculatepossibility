#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: filter_google.py
# @time: 2020-01-20 17:12
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
    with open('/Data_SSD/zhipengye/zhipengye/LM/filter_rule/WordSegDict.small',encoding='utf-8') as file:
        for line in file:
            word_set.add(line.strip())

    content_list = []
    with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/GoogleWbi-Direct',encoding='utf-8') as file:
        for line in file:
            if line.startswith('-'):
                segments = line.split('\t')
                words = segments[1].split(' ')
                if verifyContent(words, word_set):
                    content_list.append(line.strip())
            else:
                content_list.append(line.strip())
            if len(content_list) >= 10000000:
                with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/GoogleWbi-Direct.small','a',encoding='utf-8') as file:
                    file.write('\n'.join(content_list))
                    content_list = []
                    print('10000000 have been processed')

    with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/GoogleWbi-Direct.small', 'a',encoding='utf-8') as file:
        file.write('\n'.join(content_list))
        print(str(len(content_list))+' have been processed')
