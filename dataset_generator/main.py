import os
import math
import random

def generate_unsorted_dataset(size):
    rows_count = math.ceil(size / 10)

    for i in range(rows_count):
        row = []
        is_last_row = i == rows_count - 1
        last_row_shorter = size % 10 != 0
        shorter_line = is_last_row and last_row_shorter
        row_columns_count = 10 if not shorter_line else size % 10

        for j in range(row_columns_count):
            generated_random_number = random.randint(0, size)
            row.append(generated_random_number)

        string_row = ",".join(str(x) for x in row)

        with open(f"{size}.txt", "a") as file:
            if string_row:
                file.write(f"{string_row}\n")

if __name__ == "__main__":
    folder_path = "trabalho-esquenta/data/unsorted"
    files_in_directory = os.listdir(folder_path)

    for file_name in files_in_directory:
        if not file_name.endswith(".txt"):
            continue

        number_string = file_name.split(".")[0]
        number = int(number_string)

        print(f"Generating dataset for {number}...")
        generate_unsorted_dataset(number)

