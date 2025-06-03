import re

class ConfigFileHandler:
    def __init__(self, filename: str):
        self.fd = open(filename, "r+")
        self.config = {}
        self.config.update(map(
            lambda line: line.strip().split("=", 1),
            self.fd.readlines()
        ))

    def __del__(self):
        self.fd.close()

    def __getitem__(self, key):
        return self.config[key]

    def __update_file(self):
        self.fd.seek(0)
        self.fd.truncate()
        print("\n".join(f"{key}={value}"
                        for key, value in self.config.items()
                        ), file=self.fd)
        self.fd.flush()

    def __setitem__(self, key, value):
        self.config[key] = value
        self.__update_file()

    def __delitem__(self, key):
        del self.config[key]
        self.__update_file()

if __name__ == "__main__":
    handler = ConfigFileHandler("config")
    del handler["network"]