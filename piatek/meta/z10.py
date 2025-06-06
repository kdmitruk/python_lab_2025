class ConfigFileHandler:
    data = {}
    path = ''
    def __init__(self, path):
        self.path = path
        file = open(path, 'r')
        for line in file.readlines():
            #line = line.strip()
            line_items = line.split(':')
            self.data[line_items[0]] = line_items[1].strip()
        print(self.data)
        file.close()

    def __getitem__(self, key):
        return self.data[key]

    def update_file(self):
        file = open(self.path, 'w')
        for key, value in self.data.items():
            file.write(f'{key}: {value} \n')
        file.close()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.update_file()

    def __delitem__(self, key):
        del self.data[key]
        self.update_file()

def main():
    config = ConfigFileHandler('data.txt')
    k1 = config['klucz1']
    config['klucz1'] = "asdasdw"
    print(k1)
    del config['klucz2']

if __name__ == '__main__':
    main()