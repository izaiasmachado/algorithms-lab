import os
from utils import logger, format_number, Complexity

from algorithms import find_max_value_v1, find_max_value_v2
from execution.instance import Instance
from execution.algorithm import Algorithm, AlgorithmCollection
from execution import Dataset, DatasetGroup, DatasetGroupCollection
from execution.instance import InstanceExecutor

class SearchAlgorithmsInstanceExecutor(InstanceExecutor):
    def __init__(self, algorithm_collection, dataset_group_collection):
        super().__init__(algorithm_collection, dataset_group_collection)
        self.create_instances()

    def create_instances(self):
        for dataset in self.dataset_collection.get_datasets():
            for algorithm in self.algorithm_collection.get_algorithms():
                for _ in range(100):
                    algorithm_name = algorithm.get_name()
                    instance = Instance(algorithm, dataset)
                    self.instances.append(instance)

    def execute(self):
        sorted_instances = sorted(self.instances, key=lambda instance: instance.complexity_steps())

        for i, instance in enumerate(sorted_instances):
            output = instance.execute()

            uuid = instance.get_uuid()
            dataset = instance.get_dataset()
            dataset_name = dataset.get_name()
            dataset_type = dataset.get_dataset_type()
            algorithm_name = instance.get_algorithm().get_name()
            formated_execution_time = format_number(instance.get_execution_time())
            formated_peak_memory_usage = format_number(instance.peak_memory_usage)
            complexity_steps = instance.complexity_steps()

            logger.info(f"Instance {i + 1} of {len(sorted_instances)}")
            logger.info(f"Algorithm: {instance.get_algorithm().get_name()}")
            logger.info(f"Dataset: {instance.get_dataset().get_name()}")
            logger.info(f"Complexity Steps: {complexity_steps}")

            with open(f'data/output.csv', 'a') as file:
                file.write(f"{uuid},{dataset_type},{algorithm_name},{dataset_name},{formated_execution_time},{formated_peak_memory_usage},{complexity_steps},{output}\n")

            logger.info(f"Output: {output}")
            logger.info(f"Execution Time: {formated_execution_time}")
            logger.info(f"Peak Memory Usage: {formated_peak_memory_usage}")
            logger.info(f'{"-" * 50}')

if __name__ == "__main__":
    dataset_group_collection_path = os.path.abspath("data")
    dataset_group_folder_names = ["unsorted"]
    
    algorithm_collection = AlgorithmCollection()
    dataset_group_collection = DatasetGroupCollection(dataset_group_collection_path, dataset_group_folder_names)

    algorithm_collection.add_algorithm("Max Value - v1", find_max_value_v1, Complexity.o_n)
    algorithm_collection.add_algorithm("Max Value - v2", find_max_value_v2, Complexity.o_n_log_n)

    executor = SearchAlgorithmsInstanceExecutor(algorithm_collection, dataset_group_collection)
    executor.execute()
