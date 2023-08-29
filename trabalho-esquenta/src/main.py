import os
import math
from utils import format_number
from utils.logger import logger

from algorithms import linear_search_fast_return, linear_search_slow_return, binary_search, ternary_search, quadratic_search, cubic_search
from execution.instance import Instance
from execution.algorithm import Algorithm, AlgorithmCollection
from execution import Dataset, DatasetGroup, DatasetGroupCollection
from execution.instance import InstanceExecutor


def o_log_n(n):
    return math.log(n, 2)

def o_n(n):
    return n

def o_n_squared(n):
    return n * n

def o_n_cubed(n):
    return n * n * n

class SearchAlgorithmsInstanceExecutor(InstanceExecutor):
    def __init__(self, algorithm_collection, dataset_group_collection):
        super().__init__(algorithm_collection, dataset_group_collection)
        self.create_instances()
        self.set_input_for_instances()

    def create_instances(self):
        for dataset in self.dataset_collection.get_datasets():
            for algorithm in self.algorithm_collection.get_algorithms():
                for _ in range(10):
                    algorithm_name = algorithm.get_name()
                    is_binary_search = algorithm_name == "Binary Search - Middle Element" or algorithm_name == "Binary Search - First Element" 
                    is_ternary_search = algorithm_name == "Ternary Search"
                    should_create_unsorted_instance = dataset.get_dataset_type() == "unsorted"

                    if (is_ternary_search or is_binary_search) and should_create_unsorted_instance:
                        continue
                
                    instance = Instance(algorithm, dataset)
                    too_much_memory_usage = instance.complexity_steps() > 1000000000 
                    # 2500000000

                    if too_much_memory_usage:
                        continue
                    
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
        sorted_instances = sorted(self.instances, key=lambda instance: instance.complexity_steps())

        for i, instance in enumerate(sorted_instances):
            instance.execute()

            uuid = instance.get_uuid()
            dataset = instance.get_dataset()
            dataset_name = dataset.get_name()
            dataset_type = dataset.get_dataset_type()
            algorithm_name = instance.get_algorithm().get_name()
            input_element = instance.get_input()
            formated_execution_time = format_number(instance.get_execution_time())
            formated_peak_memory_usage = format_number(instance.peak_memory_usage)
            complexity_steps = instance.complexity_steps()

            logger.info(f"Instance {i + 1} of {len(sorted_instances)}")
            logger.info(f"Algorithm: {instance.get_algorithm().get_name()}")
            logger.info(f"Dataset: {instance.get_dataset().get_name()}")
            logger.info(f"Input: {instance.get_input()}")
            logger.info(f"Complexity Steps: {complexity_steps}")

            with open(f'data/output.csv', 'a') as file:
                file.write(f"{uuid},{dataset_type},{algorithm_name},{dataset_name},{input_element},{formated_execution_time},{formated_peak_memory_usage},{complexity_steps}\n")

            logger.info(f"Execution Time: {formated_execution_time}")
            logger.info(f"Peak Memory Usage: {formated_peak_memory_usage}")
            logger.info(f'{"-" * 50}')


if __name__ == "__main__":
    algorithm_collection = AlgorithmCollection()
    dataset_group_collection = DatasetGroupCollection()

    algorithm_collection.add_algorithm("Linear Search - v1", linear_search_fast_return, o_n)
    algorithm_collection.add_algorithm("Linear Search - v2", linear_search_slow_return, o_n)
    algorithm_collection.add_algorithm("Binary Search - Middle Element", binary_search, o_log_n)
    algorithm_collection.add_algorithm("Binary Search - First Element", binary_search, o_log_n)
    algorithm_collection.add_algorithm("Ternary Search", ternary_search, o_log_n)
    algorithm_collection.add_algorithm("Quadratic Search", quadratic_search, o_n_squared)
    algorithm_collection.add_algorithm("Cubic Search", cubic_search, o_n_cubed)

    executor = SearchAlgorithmsInstanceExecutor(algorithm_collection, dataset_group_collection)
    executor.execute()
