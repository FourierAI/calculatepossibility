#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: countngram.py
# @time: 2020-01-10 20:11
# @desc:

import re

if __name__ == "__main__":

    ngram1 = 0
    ngram2 = 0
    with open('new_output1.txt') as file:
        for line in file:
            if re.match('^-[0-9]{1,}.[0-9]{1,}[\s\t]{1,}[\u4e00-\u9fa5]{1,}[\s\t]{1,}-[0-9]{1,}', line):
                ngram1 = ngram1 + 1
            if re.match('^-[0-9]{1,}.[0-9]{1,}[\s\t]{1,}[\u4e00-\u9fa5]{1,}[\s\t]{1,}[\u4e00-\u9fa5]{1,}', line):
                ngram2 = ngram2 + 1

    print('ngram1 = ', ngram1)
    print('ngram2 = ', ngram2)
