try:
    # Ask for filenames
    input_file = input("Enter the file to read: ")
    output_file = input("Enter the file to write: ")

    # Read and modify content
    with open(input_file, 'r') as infile:
        content = infile.read().upper()  # Convert to uppercase

    # Write modified content
    with open(output_file, 'w') as outfile:
        outfile.write(content)

    print(f"Content written to {output_file} successfully.")

except FileNotFoundError:
    print("Error: The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

