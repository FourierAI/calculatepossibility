#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: calculate_ngram3.py
# @time: 2020-01-14 01:27
# @desc:

import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

if __name__ == "__main__":

    content_list = []
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count.out') as file:
        for line in file:
            if line != '\n':
                content_list.append(line)
    
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count','w') as file:
        file.write(''.join(content_list))
