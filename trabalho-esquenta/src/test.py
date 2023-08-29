# from data/output.csv,
# remove all rows that have unsorted,Ternary Search

def main():
    file_path = "data/output.csv"

    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = [line for line in lines if "unsorted,Ternary Search" not in line]

    with open('data/test.csv', "w") as file:
        for line in lines:
            file.write(line)

if __name__ == "__main__":
    main()