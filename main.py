import os
def delete_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        else:
            print(f"{file_path} does not exist.")
def create_file(file_path):
    print(f"{file_path} does not exist. Creating {file_path}.")
    with open(file_path, 'w') as f:
        while True:
            line = input(f"Enter data for {file_path} (type 'done' to finish): ")
            if line.lower() == 'done':
                break
            f.write(line + '\n')
def get_file_data(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()
def check_files(ram_file, sheets_file, output_file):
    ram_data = get_file_data(ram_file)
    sheets_data = get_file_data(sheets_file)
    missing_in_ram = [line for line in sheets_data if line not in ram_data]
    missing_in_sheets = [line for line in ram_data if line not in sheets_data]
    if not missing_in_ram and not missing_in_sheets:
        return "No missing data"
    else:
        with open(output_file, 'w') as f:
            if missing_in_ram:
                f.write("Missing in Main.txt:\n")
                for line in missing_in_ram:
                    f.write(line + '\n')
            if missing_in_sheets:
                f.write("\nMissing in Check.txt:\n")
                for line in missing_in_sheets:
                    f.write(line + '\n')
        return "Missing data found. Please check MissingData.txt"
def main():
    ram_file = 'Main.txt'
    sheets_file = 'Check.txt'
    output_file = 'MissingData.txt'
    delete_files([ram_file, sheets_file, output_file])
    create_file(ram_file)
    create_file(sheets_file)
    result = check_files(ram_file, sheets_file, output_file)
    print(result)
    input("Press Enter to continue...")
if __name__ == "__main__":
    main()
