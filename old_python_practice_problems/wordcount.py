file_path = "D:\\Data_Engineer_perp\\grow_data_skills\\pyspark\\experimentation\\python\\file1.txt"
words = []
with open(file_path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into words and extend the list
        words.extend(line.split())

# Print the list of words
print(words)

