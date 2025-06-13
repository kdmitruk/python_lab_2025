class RollingAvg:
    def __init__(self, size):
        self.size = size


    def __call__(self, data):
        result = []
        for i in range(len(data)):
            window = data[max(0, i-self.size + 1): i+1]
            avg = sum(window) / len(window)
            result.append(avg)
        return result

def main():
    l = [45, 657,2, 78,9, 8,54,52 ,547 ,6798 -0, 5, 23, 1]
    l = list(map(RollingAvg(4), [l]))
    # ravg = RollingAvg(4)
    # l = ravg(l)
    print(l)

if __name__ == '__main__':
    main()