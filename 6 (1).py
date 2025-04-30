# Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other, the remaining lines from the larger file should be simply copied into the target file.

file1 = '10 File hendling/6th/1.txt'
file2 = '10 File hendling/6th/2.txt'
output_file = '10 File hendling/6th/mergedfile.txt'

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    with open(output_file, 'w') as output:
        min_lines = min(len(lines1), len(lines2))
        
        for i in range(min_lines):
            output.write(lines1[i].strip() + '\n') 
            output.write(lines2[i].strip() + '\n')  

        if len(lines1) > len(lines2):
            output.writelines(lines1[min_lines:])
        elif len(lines2) > len(lines1):
            output.writelines(lines2[min_lines:])

    print("Files merged successfully!")

except FileNotFoundError:
    print("One of the files was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
