<table>
<tr>
<td>
This script is a basic example of the Python programming language. It was created for personal use, but feel free to use or study it
</td>
</tr>
</table>

---

## Features

- Function Definition: The function check_files takes two arguments: ram_file and sheets_file, which are the paths to the two text files to be compared.
- Read Files: It opens and reads the contents of both files. Each file's content is read line by line and stored in lists.
- Comparison: The function compares these lists (which contain the lines of each file) to check if they are identical.
- Return Value: If the contents of both files are the same, it returns "Ok"; otherwise, it returns "No".
- Execution: The function is then called with Main.txt and Check.txt as arguments, and the result is printed.

## Code Example:

```python
def check_files(ram_file, sheets_file):
    # Open the file specified by `ram_file` in read mode ('r') and assign it to variable `f`.
    # Read the contents of the file, split it into lines (by newline characters), and store it in `ram_data`.
    with open(ram_file, 'r') as f:
        ram_data = f.read().splitlines()

    # Open the file specified by `sheets_file` in read mode ('r') and assign it to variable `f`.
    # Read the contents of the file, split it into lines (by newline characters), and store it in `sheets_data`.
    with open(sheets_file, 'r') as f:
        sheets_data = f.read().splitlines()

    # Compare the content of `ram_data` and `sheets_data`.
    # If they are the same, return the string "Ok".
    # Otherwise, return the string "No".
    if ram_data == sheets_data:
        return "Ok"
    else:
        return "No"

# Define the file paths to be compared.
ram_file = 'Main.txt'
sheets_file = 'Check.txt'

# Call the `check_files` function with `ram_file` and `sheets_file` as arguments.
# Store the result of this function call in the variable `result`.
result = check_files(ram_file, sheets_file)

# Print the result to the console.
print(result)
```
