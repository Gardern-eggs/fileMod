def read_and_modify_file():
    try:
        # Prompt the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        print(f"Attempting to open file: {input_filename}")
        # Attempt to open and read the input file
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        print("File read successfully.")
        
        # Modify the content (for example, make all text uppercase)
        modified_lines = [line.upper() for line in lines]
        
        # Prompt the user for the output filename
        output_filename = input("Enter the name of the file to write the modified content: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.writelines(modified_lines)
        
        print(f"Modified content successfully written to '{output_filename}'.")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read/write the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
