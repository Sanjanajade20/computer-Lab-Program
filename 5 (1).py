source_file = '10 File hendling/5th/programme5.txt'
destination_file = '10 File hendling/destination.txt'

try:
    with open(source_file, 'r') as src:
        content = src.read()
    content_upper = content.upper()
    
    with open(destination_file, 'w') as dest:
        dest.write(content_upper)

    print("Content copied and converted to uppercase successfully!")

except FileNotFoundError:
    print(f"Error: The file '{source_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
