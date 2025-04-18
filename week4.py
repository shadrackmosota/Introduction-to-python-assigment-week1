def read_modify_write():
    try:
        # Ask user for filename
        filename = input("Please enter the filename: ")
        # Check if file exists
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist.")
            return
        # Try to read the file
        with open(filename, 'r') as file:
            file_content = file.read()
        # Modify the content by adding a line at the beginning
        modified_content = "This is a new line at the beginning\n" + file_content
        # Write to a new file
        output_filename = f"modified_{filename}"
        with open(output_filename, 'w') as output:
            output.write(modified_content)
        print(f"Successfully created a modified version of '{filename}' as '{output_filename}'")
    except IOError as e:
        print(f"Error {e}: Unable to read '{filename}'")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main execution
if __name__ == "__main__":
    read_modify_write()
