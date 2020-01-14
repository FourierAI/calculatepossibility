
import os
import re

class LanguageModelContent:

    def __init__(self, words,count):
        self.words = words
        self.count = count

    def __str__(self):
        return self.words  + '\t' +self.count

if __name__ == "__main__":
    
    dir_list = sorted(os.listdir('/home/fourier/Data/data'))
    # because ngrams-[00030 - 00036]-of-00394 have no invalid  data
    filtered_list = [dir for dir in dir_list if dir >= 'ngrams-00001-of-00394' and dir <= 'ngrams-0029-of-00394']

    for file_name in filtered_list:
        grams_2 = []
        with open('/home/fourier/Data/data/'+ file_name) as file:
            for line in file:
                if re.match('^[\u4e00-\u9fa5]{1,8}[\s\t]{1,}[\u4e00-\u9fa5]{1,8}[\s\t]{1,}\d{1,}', line):
                    segments = line.split('\t')
                    words = segments[0]
                    count = segments[1]
                    model = LanguageModelContent(words, count)
                    grams_2.append(model)

        if len(grams_2) == 0:
            continue

        with open('/home/fourier/Data/processed_file/gram2'+ file_name, 'a') as file:
            print(file_name+'has been started!')
            for model in grams_2:
                file.write(str(model) + '\n')
            print(file_name+'has been processed!')

    



