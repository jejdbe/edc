
class DataReader:

    @staticmethod
    def read(path: str):
        f = open(path)
        data = f.read()
        f.close()
        return data
