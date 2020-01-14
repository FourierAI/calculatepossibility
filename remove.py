
if __name__ == "__main__":

    content_list = []
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count.out') as file:
        for line in file:
            if line != '\n':
                content_list.append(line)
    
    with open('/Data_SSD/zhipengye/zhipengye/data/gram2/gram2_count','w') as file:
        file.write(''.join(content_list))
