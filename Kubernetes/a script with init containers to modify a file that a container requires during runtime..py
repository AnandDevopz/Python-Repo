import os

# Define the path to the file you want to modify
FILE_PATH = "/path/to/your/file.txt"

def modify_file():
    try:
        # Open the file in write mode
        with open(FILE_PATH, 'w') as file:
            # Write or modify the content as needed
            file.write("Hello, World!\nModified by init container.")

        print(f"File {FILE_PATH} modified successfully.")
    except Exception as e:
        print(f"Error modifying the file: {str(e)}")

if __name__ == "__main__":
    modify_file()
