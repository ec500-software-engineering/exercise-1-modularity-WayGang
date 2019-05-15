# copyright @Kainan Liu @Wenjie Luo
def read_data(path):
    try:
        with open(path, 'r') as f:
            time = []
            value = []
            data = f.readline().split()
            while data:
                if data:
                    time.append(data[0])
                    value.append(float(data[1]))


                else:
                    print("Empty data file!\n")
                    return 2
                data = f.readline().split()
        if 'bo' in path:
            print("Read blood oxygen data successfully")
        elif 'bp' in path:
            print("Read blood pressure data successfully")
        elif 'pul' in path:
            print("Read pulse data successfully")
        return value
    except:
        print("Error:No input data\n")


if __name__ == '__main__':
    read_data('./bo.txt')