import re


if __name__ == "__main__":

    content = []
    count = 0
    count_line = 0
    trigger = True
    with open('/home/fourier/Data/processed_file/data/GoogleWbi-Direct') as file:
        for line in file:  

            if trigger and ('-99' in line):
                content.append(line)

            if '2-grams' in line:
                with open('ngram_1.txt','w') as file:
                    file.write('\n'.join(content))
                    print('ngram_1 process successfully')
                content = []
                ngram_1_trigger = True
                trigger = False

            if not trigger and ('end' not in line):
                content.append(line)

            if len(content) >= 10000000:
                count = count +1
                with open('ngram_2_'+str(count)+'.txt','w') as file:
                    file.write('\n'.join(content))
                print('ngram_2 have processed 10000000 rows')
                content = []

    with open('ngram_2_'+str(count)+'.txt','w') as file:
        file.write('\n'.join(content))
        print('ngram_2 process successfully')
        print(len(content))



            
