import os
from utils.logger import logger
from execution import ExecutionInstance, Dataset, DatasetGroup, DatasetGroupCollection
from utils import get_data_from_file, File, Folder

# table that writes fast to csv

class Table:
    def __init__(self, name):
        self.name = name


# def test():
#     dataset_collection = DatasetGroupCollection()
#     groups = dataset_collection.get_groups()
#     datasets = dataset_collection.get_datasets()

#     print("Sorted/Unsorted,Dataset Name,Full Path")
#     for dataset in datasets:
#         dataset_name = dataset.get_name()
#         dataset_type = dataset.get_dataset_type()
#         dataset_path = dataset.get_path()

#         logger.info(f"{dataset_type},{dataset_name},{dataset_path}")
