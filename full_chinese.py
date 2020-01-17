#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: full_chinese.py
# @time: 2020-01-17 17:19
# @desc:

import os
import re

if __name__ == "__main__":

    files_name = sorted(os.listdir('/Data_SSD/zhipengye/zhipengye/LM/processed_data/small_dictory_filtered'))

    for file_name in files_name:
        content_list = []
        with open('/Data_SSD/zhipengye/zhipengye/LM/processed_data/small_dictory_filtered/'+file_name, encoding='utf-8') as file:
            for line in file:
                segments = line.split('\t')
                words = segments[0].replace(' ','')

                if re.match('^[\u4e00-\u9fa5]{1,}$',words):
                    content_list.append(line.strip())
        with open('/Data_SSD/zhipengye/zhipengye/LM/processed_data/small_full_chinese_filtered/'+file_name, 'a',encoding='utf-8') as file:
            file.write('\n'.join(content_list))

    print('Program is ok!')