import uuid
import time
from utils.logger import logger
from utils import get_data_from_file, Folder

class Dataset:
    def __init__(self, file):
        self.set_file(file)
        self.data = self.get_data()

    def set_file(self, file):
        self.file = file

        dataset_type = self.file.folder.get_name()
        self.set_dataset_type(dataset_type)

    def set_dataset_type(self, dataset_type):
        self.dataset_type = dataset_type

    def get_file(self):
        return self.file

    def get_name(self):
        file_name = self.file.get_name()
        name = file_name.replace(".txt", "")
        return name

    def get_path(self):
        file = self.get_file()
        folder_path = file.get_path()
        file_name = file.get_name()
        path = f"{folder_path}/{file_name}"
        return path

    def get_data(self):
        file = self.get_file()
        file_path = file.get_path()
        file_name = file.get_name()
        
        if hasattr(self, "data"):
            return self.data

        file_full_path = f'{file_path}/{file_name}'
        data = get_data_from_file(file_full_path)
        return data

    def get_input_size(self):
        data = self.get_data()
        input_size = len(data)
        return input_size

    def get_dataset_type(self):
        return self.dataset_type

    # it has a file class
    #   - Input Size
    #   - Path to the dataset
    #   - Sorted/Unsorted

# dataset group will recieve a path to a folder
# it will have a list of datasets
class DatasetGroup:
    def __init__(self, folder):
        self.folder = folder

    def get_datasets(self):
        datasets = []
        files = self.folder.get_files_from_directory()
        text_files = list(filter(lambda file: file.get_name().endswith(".txt"), files))
        sorted_text_files = sorted(text_files, key=lambda file: int(file.get_name().replace(".txt", "")))

        for file in sorted_text_files:
            dataset = Dataset(file)
            datasets.append(dataset)

        return datasets


class DatasetGroupCollection:
    def get_dataset_folders(self):
        folders_path = "data"
        dataset_group_folder_names = [
            "sorted",
            "unsorted"
        ]

        folders = []
        for dataset_folder_name in dataset_group_folder_names:
            folder = Folder(f"{folders_path}/{dataset_folder_name}")
            folders.append(folder)

        return folders

    def get_groups(self):
        folders = self.get_dataset_folders()
        groups = []

        for folder in folders:
            group = DatasetGroup(folder)
            groups.append(group)

        return groups

    def get_datasets(self):
        groups = self.get_groups()
        datasets = []

        for group in groups:
            group_datasets = group.get_datasets()
            datasets.extend(group_datasets)

        return datasets
