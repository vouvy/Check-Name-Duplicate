def check_files(ram_file, sheets_file):
    with open(ram_file, 'r') as f:
        ram_data = f.read().splitlines()
    with open(sheets_file, 'r') as f:
        sheets_data = f.read().splitlines()
    if ram_data == sheets_data:
        return "Ok"
    else:
        return "No"
ram_file = 'Main.txt'
sheets_file = 'Check.txt'
result = check_files(ram_file, sheets_file)
print(result)
