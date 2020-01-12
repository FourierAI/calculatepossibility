#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: deduplication.py
# @time: 2020-01-09 23:20
# @desc:

import re


def verifyContent(chinese_content, verify_map):
    for words in chinese_content:
        for single_word in words:
            value = verify_map.get(single_word)
            if value == None:
                return False
    return True


if __name__ == "__main__":

    verify_map = {}
    with open('GB_7356-Ch.txt') as file:
        for line in file:
            verify_map[line.strip('\n')] = 0

    count_line = 0
    count = 0
    output_content = []
    with open('output.txt') as file:
        for line in file:
            count_line = count_line + 1
            count = count + 1
            if re.match("^-", line):
                chinese_content = re.findall('[\u4e00-\u9fa5]{1,}', line)
                isincludedinfile = verifyContent(chinese_content, verify_map)
                if isincludedinfile:
                    output_content.append(line)
            else:
                output_content.append(line)

            if count >= 10000000 and count_line <=250000000:
                print('10000000 rows have been processed')
                file_content = str.join('', output_content)
                with open('new_output1.txt', 'a') as file:
                    file.write(file_content)
                # remove buffer
                output_content = []
                count = 0
            if count_line >= 250000000 and count >= 3805312:
                print('3805312 rows have been processed')
                file_content = str.join('', output_content)
                with open('new_output1.txt', 'a') as file:
                    file.write(file_content)

    print("Programme is gone!")
