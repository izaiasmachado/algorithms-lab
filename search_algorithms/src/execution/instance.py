import uuid
import time
import tracemalloc
from utils.logger import logger
from utils import get_data_from_file

class Instance:
    def __init__(self, algorithm, dataset):
        self.uuid = uuid.uuid4()
        self.algorithm = algorithm
        self.dataset = dataset
        self.input = None

    def get_uuid(self):
        return self.uuid

    def get_algorithm(self):
        return self.algorithm

    def get_dataset(self):
        return self.dataset

    def get_params(self):
        data = self.dataset.get_data()
        params = [data]

        if self.input is None:
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

        tracemalloc.start()
        start = time.time()
        self.algorithm.run(*params)
        end = time.time()

        _, self.peak_memory_usage = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.execution_time = end - start

    def get_execution_time(self):
        return self.execution_time

    def complexity_steps(self):
        dataset_size = self.dataset.get_input_size()
        return self.algorithm.get_steps(dataset_size)

class InstanceExecutor:
    def __init__(self, algorithm_collection, dataset_collection):
        self.algorithm_collection = algorithm_collection
        self.dataset_collection = dataset_collection
        self.instances = []

    def create_instances(self):
        instances = []

        for dataset in self.dataset_collection.get_datasets():
            for algorithm in self.algorithm_collection.get_algorithms():
                instance = Instance(algorithm, dataset)
                instances.append(instance)

    def get_instances(self):
        return self.instances

    def set_input_for_instances(self):
        pass

    def execute_instances(self):
        for instance in self.instances:
            instance.execute()
