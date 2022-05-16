import os

folder_input = ''
while True:
    # Making a flag variable to prevent the program to run if the folder path is not correct.
    flag = 0
    # Making a variable that will be used to name each file.
    count = 1
    
    if folder_input == '':
        # Ask for the absolute path of the folder containing the files to be renamed.
        folder_input = input('Enter the folder path :')

        # Making the path relative, so it can be accessed.
        folder = folder_input + '\\'
    else :
        ask_par = input('Do you want to rename files in a different folder? (Y/N):')
        if ask_par == 'Y' or ask_par == 'y':
            # Ask for the absolute path of the folder containing the files to be renamed.
            folder_input = input('Enter the folder path :')

            # Making the path relative, so it can be accessed.
            folder = folder_input + '\\'
        elif ask_par == 'N' or ask_par == 'n':
            break
        else:
            print('Something went wrong. Please try again! \n')
            flag = 1
    if flag == 0:
        mode = input('Press the coresponding number to choose mode: \n 0. Rename files with ascending numerical order \n 1. Rename files keeping the first n characters \n 2. Rename files keeping the last n characters \n PRESS ENTER TO QUIT \n Mode: ')
        if mode == '':
            break
        elif mode == '0':
            # Loop for each file in the selected folder.
            for file_name in os.listdir(folder):
    
                old_name = folder + file_name
                new_name = folder + str(count) + '.txt'

                # Rename the file.
                os.rename(old_name, new_name)
                count += 1
                
            # Prints a sentence for the user, that the operation was successful.
            print('All ' + str(count - 1) + ' files are renamed.')
            print('----------------------------------------------------------------')
            print('\n')  
        elif mode == '1':
            try:
                val = input('Please insert the amount of characters you want to keep: ')
                # Loop for each file in the selected folder.
                for file_name in os.listdir(folder):
    
                    old_name = folder + file_name
                    # Creating a new file name without the extension.
                    fn_no_ext = os.path.splitext(file_name)[0]
                    # Creating a new name for the file keeping only the desired amount of characters.
                    new_name = folder + fn_no_ext[0:int(val)] + '.txt'

                    # Rename the file.
                    os.rename(old_name, new_name)
                    count += 1
                    
                # Prints a sentence for the user, that the operation was successful.
                print('All ' + str(count - 1) + ' files are renamed.')
            except:
                print('An error occured! Please try again.')
            print('----------------------------------------------------------------')
            print('\n')
        elif mode == '2':
            try:
                val = input('Please insert the amount of characters you want to keep: ')
                # Loop for each file in the selected folder.
                for file_name in os.listdir(folder):
    
                    old_name = folder + file_name
                    # Creating a new file name without the extension.
                    fn_no_ext = os.path.splitext(file_name)[0]
                    length = len(fn_no_ext)
                    # Creating a new name for the file keeping only the desired amount of characters.
                    new_name = folder + fn_no_ext[- int(val):length] + '.txt'

                    # Rename the file.
                    os.rename(old_name, new_name)
                    count += 1
                # Prints a sentence for the user, that the operation was successful.
                print('All ' + str(count - 1) + ' files are renamed.')
            except:
                print('An error occured! Please try again.')
            print('----------------------------------------------------------------')
            print('\n')
        else :
            print('Please choose a number from the list above')
            print('----------------------------------------------------------------')
            print('\n')
