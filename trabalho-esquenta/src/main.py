import os
from utils import format_number
from utils.logger import logger

from algorithms import linear_search
from execution.instance import Instance
from execution.algorithm import Algorithm, AlgorithmCollection
from execution import Dataset, DatasetGroup, DatasetGroupCollection
from execution.instance import InstanceExecutor

class SearchAlgorithmsInstanceExecutor(InstanceExecutor):
    def __init__(self, algorithm_collection, dataset_group_collection):
        super().__init__(algorithm_collection, dataset_group_collection)
        self.create_instances()
        self.set_input_for_instances()

    def create_instances(self):
        for dataset in self.dataset_collection.get_datasets():
            for algorithm in self.algorithm_collection.get_algorithms():
                algorithm_name = algorithm.get_name()
                is_binary_search = algorithm_name == "Binary Search - Middle Element" or algorithm_name == "Binary Search - First Element" 
                should_create_unsorted_instance = dataset.get_dataset_type() == "unsorted" and not is_binary_search

                if should_create_unsorted_instance:
                    continue

                instance = Instance(algorithm, dataset)
                self.instances.append(instance)

    def set_input_for_instances(self):
        for instance in self.instances:
            algorithm_name = instance.get_algorithm().get_name()
            dataset_data = instance.get_dataset().get_data()

            first_index = 0
            middle_index = int(len(dataset_data)/2)
            
            should_input_first_element = algorithm_name == "Binary Search - First Element"
            element_index = first_index if should_input_first_element else middle_index
            
            input_element = dataset_data[element_index]
            instance.set_input(input_element)

    def execute(self):
        sorted_instances = sorted(self.instances, key=lambda instance: instance.get_dataset().get_input_size())

        for instance in sorted_instances:
            instance.execute()

            formated_execution_time = format_number(instance.get_execution_time())
            formated_peak_memory_usage = format_number(instance.peak_memory_usage)

            logger.info(f"Algorithm: {instance.get_algorithm().get_name()}")
            logger.info(f"Dataset: {instance.get_dataset().get_name()}")
            logger.info(f"Input: {instance.get_input()}")
            logger.info(f"Execution Time: {formated_execution_time}")
            logger.info(f"Peak Memory Usage: {formated_peak_memory_usage}")

if __name__ == "__main__":
    algorithm_collection = AlgorithmCollection()
    dataset_group_collection = DatasetGroupCollection()

    algorithm_collection.add_algorithm("Linear Search - v1", linear_search.linear_search_fast_return)
    algorithm_collection.add_algorithm("Linear Search - v2", linear_search.linear_search_slow_return)
    # algorithm_collection.add_algorithm("Binary Search - Middle Element", linear_search.linear_search_slow_return)
    # algorithm_collection.add_algorithm("Binary Search - First Element", linear_search.linear_search_slow_return)

    executor = SearchAlgorithmsInstanceExecutor(algorithm_collection, dataset_group_collection)
    executor.execute()
