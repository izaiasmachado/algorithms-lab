import uuid
import time
from utils.logger import logger
from utils import get_data_from_file

class Instance:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.dataset = dataset
        self.execution_time = None

    def set_dataset(self, dataset):
        self.dataset = dataset

    def set_input(self, input):
        self.input = input

    def get_params(self):
        params = [self.dataset]

        if isinstance(self.input, list):
            params.extend(self.input)
        else:
            params.append(self.input)

    def execute(self):
        params = self.get_params()
        print(params)

        # start = time.time()
        # self.algorithm.run(self.get_params())
        # end = time.time()
        # self.execution_time = end - start
        # self.log()

class ExecutionInstance:
    def __init__(self):
        self.id = uuid.uuid4()
        self.function = None
        self.file_path = None
    
    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_function(self, function):
        self.function = function

    def execute(self):
        data = get_data_from_file(self.file_path)
        print(data)
        start = time.time()
        self.function(data)
        end = time.time()
        self.execution_time = end - start
        self.log()

    def log(self):
        logger.info(f"Execution ID: {self.id}")
        logger.info(f"File Path: {self.file_path}")
        logger.info(f"Execution Time: {self.execution_time}")
