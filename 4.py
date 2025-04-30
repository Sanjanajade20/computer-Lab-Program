# Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.

source_file = "10 File hendling/4th/source_folder/sample.txt"  
destination_folder = "10 File hendling/4th/New_Subdirectory"
destination_file = f"{destination_folder}/sample.txt"  

try:
    with open(source_file, 'rb') as src_file:
        content = src_file.read()

    with open(destination_file, 'wb') as dest_file:
        dest_file.write(content)

    print("File copied successfully!")

except FileNotFoundError:
    print("Error: Source file or destination folder not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

