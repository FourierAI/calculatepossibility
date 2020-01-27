#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: count_ngram.py
# @time: 2020-01-23 18:28
# @desc:



if __name__ == '__main__':

    gram1_count = 0
    gram2_count = 0
    gram3_count = 0

    with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/GoogleWbi-Direct.small',encoding='utf-8') as file:
        for line in file:
            if line.startswith('-'):
                segments = line.split('\t')
                words = segments[1].split(' ')
                if len(words) == 1:
                    gram1_count = gram1_count +1
                if len(words) == 2:
                    gram2_count = gram2_count +1
                if len(words) == 3:
                    gram3_count = gram3_count +1

    print('The count of gram1 is '+ str(gram1_count))
    print('The count of gram2 is ' + str(gram2_count))
    print('The count of gram3 is ' + str(gram3_count))