
from .data_reader import DataReader
import json

class JSONReader(DataReader):

    @staticmethod
    def read(path: str):
        data = DataReader.read(path)
        data = json.loads(data)
        return data
