<h1 align="center">
<table>
<tr>
<td>
This script is a basic example of the Python programming language It was created for personal use But feel free to use or study it
</td>
</tr>
</table>

---

<h1 align="center">
  <br>
  Features
  <br>
</h1>

> [!NOTE]  
> **This program is not designed for everyone It might seem a bit confusing I will update the program to make it more user-friendly and visually appealing next time**

* Delete Existing Files: The delete_files function deletes any files specified in the list if they exist, otherwise it informs that they do not exist.
* Create New Files: The create_file function creates a new file if it doesn’t already exist. It prompts the user to enter data line by line until they type 'done', at which point it saves the data to the file.
* Get File Data: The get_file_data function reads the contents of a file and returns it as a list of lines.
* Check Missing Data: The check_files function compares the contents of two files (a "ram" file and a "sheets" file). It identifies lines missing in each file and writes this information to an output file if there are any discrepancies.
* Main Function: The main function orchestrates the process by:
  - Deleting any existing versions of the "Main.txt", "Check.txt", and "MissingData.txt" files.
  - Creating fresh "Main.txt" and "Check.txt" files with user input.
  - Checking for missing data between the two files and reporting any discrepancies to "MissingData.txt".
  - Prompting the user to press Enter to continue at the end.

---

<h1 align="center">
  <br>
  How To Use
  <br>
</h1>

![screenshot](https://raw.githubusercontent.com/vouvy/Check-Name-Duplicate/main/Img/Check-Name-Duplicate.gif)

> [!TIP]
> **If a message appears stating 'Missing data found. Please check MissingData.txt,' it indicates that there is a data inconsistency You can verify the specific discrepancies by examining the MissingData.txt file**

> [!TIP]
> **However, if a message 'No missing data', it indicates that all data is identical**

---

<h1 align="center">
  <br>
  Code Example
  <br>
</h1>

```python
import os  # Import the os module to interact with the operating system

def delete_files(file_paths):
    # This function deletes files whose paths are given in the file_paths list
    for file_path in file_paths:
        if os.path.exists(file_path):  # Check if the file exists
            os.remove(file_path)  # Remove the file
            print(f"{file_path} has been deleted.")  # Print confirmation
        else:
            print(f"{file_path} does not exist.")  # Print a message if the file does not exist

def create_file(file_path):
    # This function creates a file at the given file_path and allows the user to input data
    print(f"{file_path} does not exist. Creating {file_path}.")
    with open(file_path, 'w') as f:  # Open the file in write mode
        while True:
            line = input(f"Enter data for {file_path} (type 'done' to finish): ")
            if line.lower() == 'done':  # Check if the user wants to finish input
                break
            f.write(line + '\n')  # Write the input data to the file

def get_file_data(file_path):
    # This function reads the contents of the file at file_path and returns it as a list of lines
    with open(file_path, 'r') as f:  # Open the file in read mode
        return f.read().splitlines()  # Read the file contents and split into a list of lines

def check_files(ram_file, sheets_file, output_file):
    # This function checks for discrepancies between two files and writes missing data to an output file
    ram_data = get_file_data(ram_file)  # Get data from the first file
    sheets_data = get_file_data(sheets_file)  # Get data from the second file
    missing_in_ram = [line for line in sheets_data if line not in ram_data]  # Find lines in the second file not in the first
    missing_in_sheets = [line for line in ram_data if line not in sheets_data]  # Find lines in the first file not in the second
    if not missing_in_ram and not missing_in_sheets:
        return "No missing data"  # If no discrepancies, return this message
    else:
        with open(output_file, 'w') as f:  # Open the output file in write mode
            if missing_in_ram:
                f.write("Missing in Main.txt:\n")  # Write header for missing data in the first file
                for line in missing_in_ram:
                    f.write(line + '\n')  # Write each missing line
            if missing_in_sheets:
                f.write("\nMissing in Check.txt:\n")  # Write header for missing data in the second file
                for line in missing_in_sheets:
                    f.write(line + '\n')  # Write each missing line
        return "Missing data found. Please check MissingData.txt"  # Inform the user about the discrepancies

def main():
    # Main function to execute the script logic
    ram_file = 'Main.txt'
    sheets_file = 'Check.txt'
    output_file = 'MissingData.txt'
    delete_files([ram_file, sheets_file, output_file])  # Delete old files if they exist
    create_file(ram_file)  # Create the first file and get input from the user
    create_file(sheets_file)  # Create the second file and get input from the user
    result = check_files(ram_file, sheets_file, output_file)  # Check for discrepancies and write them to the output file
    print(result)  # Print the result of the check
    input("Press Enter to continue...")  # Wait for the user to press Enter before exiting

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly
```
