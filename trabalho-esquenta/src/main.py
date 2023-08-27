import os
from utils.logger import logger

from algorithms import linear_search
from execution.instance import Instance
from execution.algorithm import Algorithm, AlgorithmCollection
from execution import Dataset, DatasetGroup, DatasetGroupCollection

def test_c(a, b):
    return []

if __name__ == "__main__":
    algorithm_collection = AlgorithmCollection()

    algorithm_collection.add_algorithm("a", linear_search.linear_search_fast_return)
    algorithm_collection.add_algorithm("b", linear_search.linear_search_slow_return)
    algorithm_collection.add_algorithm("c", test_c)

    datasets = DatasetGroupCollection().get_datasets()

    # For each algorithm, create the instance

    instances = []

    for dataset in datasets:
        dataset_data = dataset.get_data()
        
        for algorithm in algorithm_collection.get_algorithms():
            logger.debug(f'Creating instance for {algorithm.get_name()} and {dataset.get_name()}')
            
            middle_element = dataset_data[int(len(dataset_data)/2)]
            algorithm_name = algorithm.get_name()
            instance = Instance(algorithm)
            instance.set_dataset(dataset)
            instance.set_input(middle_element)
            instances.append(instance)

        instance_c_first_element = Instance(algorithm_collection.get_algorithm("c"))
        instance_c_first_element.set_dataset(dataset)
        instance_c_first_element.set_input(dataset_data[0])
        instances.append(instance_c_first_element)

    print(len(instances))

    # instance.execute()

    # logger.info(f"Algorithm: {algorithm.get_name()}")
    # logger.info(f"Dataset: {dataset.get_name()}")
    # logger.info(f"Input: {instance.get_input()}")
    # logger.info(f"Execution Time: {instance.get_execution_time()}")

    
    # algorithm = Algorithm("Linear Search", linear_search.linear_search_fast_return)
    # instance = Instance(algorithm)
    # instance.set_dataset(dataset)
    
    # data = dataset.get_data()
    # first_element = data[0]

    # instance.set_input(first_element)
    # instance.execute()

# def test(data):
#     print(data)

# def batch_executions():
#     # files = get_files_from_directory("data/sorted")
#     sorted_files = ['100000000.txt']
    
#     for file in sorted_files:
#         ei = ExecutionInstance()
#         ei.set_file_path("data/sorted/100000000.txt")
#         ei.set_function(test)
#         ei.execute()