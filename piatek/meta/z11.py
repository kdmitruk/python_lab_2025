class RollingAvg:
    def __init__(self,size):
        self.size=size

    def __call__(self,data):
        #data = list(map(lambda value: value+self.size, data))
        result = []
        for i in range(1, len(data)-1):
            result += [(data[i-1] + data[i] + data[i+1])/3]
        return [data[0]] + result + [data[-1]]

def main():
    data = [0,1,3,3,4,15,6,7,81,9]
    data = list(map(RollingAvg(5), [data]))
    print(data)


if __name__ == '__main__':
    main()