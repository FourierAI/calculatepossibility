if __name__ == "__main__":

    count = 0
    with open(
            '/home/fourier/Data/processed_file/data/GoogleWbi-Direct_Filtered'
    ) as file:
        for line in file:
            count = count + 1
            print(line)
            if count > 1000:
                break