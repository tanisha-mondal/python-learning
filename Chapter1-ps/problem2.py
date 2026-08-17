import os

# Specify the directory path
path = r"F:\tanisha\Chapter1-ps"

# Get the list of files and directories
contents = os.listdir(path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)