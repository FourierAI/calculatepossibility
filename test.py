#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: test.py
# @time: 2020-01-12 16:49
# @desc:

if __name__ == "__main__":

    content_list = []
    count =0
    with open('/home/fourier/Data/data/ngrams-00000-of-00394') as file:
        for line in file:
            content_list.append(line)
            count = count +1
            if count > 1000:
                break

    with open('/home/fourier/Data/data/test','a') as file:
        file.write(str.join('',content_list))