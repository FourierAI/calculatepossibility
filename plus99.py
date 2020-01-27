#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: plus99.py
# @time: 2020-01-24 13:56
# @desc:

if __name__ == '__main__':

    content_list = []
    with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/n-gram3/GoogleWbi-Direct.small',encoding='utf-8') as file:
        for line in file:
            if line.startswith('-') and '-99' not in line:
                line_content = line.strip()+'\t'+'-99'
                content_list.append(line_content)
            else:
                content_list.append(line.strip())

        if len(content_list) >= 10000000:
            with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/n-gram3/GoogleWbi-Direct-99.small','a',encoding='utf-8') as file:
                file.write('\n'.join(content_list))
            print('10000000 rows have been processed!')
            content_list = []

    with open('/Data_SSD/zhipengye/zhipengye/LM/completed.data/data/n-gram3/GoogleWbi-Direct-99.small', 'a',
              encoding='utf-8') as file:
        file.write('\n'.join(content_list))
        print(str(len(content_list))+' rows have been processed!')