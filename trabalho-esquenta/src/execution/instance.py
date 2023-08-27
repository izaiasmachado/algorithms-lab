import uuid
import time
from utils.logger import logger
from utils import get_data_from_file

class Instance:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.input = None

    def set_dataset(self, dataset):
        self.dataset = dataset

    def get_params(self):
        data = self.dataset.get_data()
        params = [data]

        if not self.input:
            return params

        if isinstance(self.input, list):
            params.extend(self.input)
        else:
            params.append(self.input)

        return params

    def set_input(self, input):
        self.input = input

    def get_input(self):
        return self.input

    def execute(self):
        params = self.get_params()

        start = time.time()
        self.algorithm.run(*params)
        end = time.time()

        self.execution_time = end - start

    def get_execution_time(self):
        return self.execution_time