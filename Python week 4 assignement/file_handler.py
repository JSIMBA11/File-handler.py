# File Handling and Exception Handling Assignment
# Author: Jerald Hindia

def file_read_write():
    """
    The below code reads file contents provided by a user and writes a modified version to a new file.
    """

    # Ask user for input file name
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as infile:
            content = infile.readlines()

        # Modify the content (Example: add line numbers and uppercase)
        modified_content = []
        for index, line in enumerate(content, start=1):
            modified_content.append(f"{index}: {line.strip().upper()}\n")

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.writelines(modified_content)

        print(f"File processed successfully! Modified file saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
if __name__ == "__main__":
    file_read_write()
