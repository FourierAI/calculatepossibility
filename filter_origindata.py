#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: filter_origindata.py
# @time: 2020-01-16 12:23
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

    files_name = sorted(os.listdir('/Data_SSD/zhipengye/zhipengye/data/original_data/Data/data'))

    filtered_list = [dir for dir in files_name if dir >= 'ngrams-00000-of-00394' and dir <= 'ngrams-00132-of-00394']

    for file_name in filtered_list:
        content_list = []
        with open('/Data_SSD/zhipengye/zhipengye/data/original_data/Data/data/'+file_name,encoding='utf-8') as file:
            for line in file:
                segments = line.split('\t')
                words = segments[0].split(' ')
                flag = verifyContent(words, word_set)
                if flag:
                    content_list.append(line.strip())
        with open('/Data_SSD/zhipengye/zhipengye/data/original_data/Data/filtered_file/'+file_name,'a',encoding='utf-8') as file:
            file.write('\n'.join(content_list))

    print('Program is Ok!')
