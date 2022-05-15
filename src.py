import os

# Ask for the absolute path of the folder containing the files to be renamed.
folder_input = input('Enter the folder path :')

# Making the path relative, so it can be accessed.
folder = folder_input + '\\'

# Making a variable that will be used to name each file.
count = 1

# Loop for each file in the selected folder.
for file_name in os.listdir(folder):
    
    old_name = folder + file_name
    new_name = folder + str(count) + '.txt'

    # Rename the file.
    os.rename(old_name, new_name)
    count += 1

# Prints a sentence for the user, that the operation was successful.
print('All ' + str(count - 1) + ' files are renamed')
while True:
    exit_par = input('Press ENTER to exit')
    if (exit_par == ''):
        break
