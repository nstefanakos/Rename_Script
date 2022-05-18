import os
import time
try :
    from tkinter import Tk, filedialog
except :
    print('You are currently not using Python 3. Update your python version or paste the desired folder path when prompted. \n')
    ask = input('Continue ? (Y/N): ')
    if ask == 'Y' or 'y':
        pass
    elif ask == 'N' or 'n':
        exit()
    else :
        print('Wrong Input, only Y or y and N or n are accepted as answers. Exiting program in 3 seconds.')
        time.sleep(3)
        exit()

def access_folder():
    try:
        # Pointing root to Tk() to use it as Tk() in program.
        root = Tk()

        # Hides small tkinter window.
        root.withdraw()

        # Opened windows will be active above all windows despite selection.
        root.attributes('-topmost', True)

        # Returns opened path as str.
        folder_input = filedialog.askdirectory()

        # Making the path relative, so it can be accessed.
        folder = folder_input + '\\'
        return folder, folder_input
        
    except :
        # Ask for the absolute path of the folder containing the files to be renamed.
        folder_input = input('Enter the folder path :')

        # Making the path relative, so it can be accessed.
        folder = folder_input + '\\'
        return folder, folder_input

def f_rename(old_name,new_name,count,error_count):
    try :
        # Rename the file.
        os.rename(old_name, new_name)
        count += 1
        error_count = 1
        return count
    except FileExistsError:
        error_count +=1
        new_name_2 = folder + str(count) + '(' + str(error_count) + ')' + '.txt'
        name_ask = input('The file ' + new_name + ' already exists, do you want to rename it as ' + new_name_2 + '? (Y/N): ')
        if name_ask == 'Y' or name_ask == 'y':
            # Call rename function
            f_rename(old_name, new_name_2, count, error_count)
            return count
        elif name_ask == 'N' or name_ask == 'n':
            return count
        else:
            print('Wrong input. Program will exit in 5 seconds to prevent any further confusion!')
            time.sleep(5)
            exit()
    except :
        print('Something went wrong with the file ' + old_name + '!')

def f_rename_2(old_name,new_name,val,mode,count,error_count):
    try :
        # Rename the file.
        os.rename(old_name, new_name)
        count += 1
        error_count = 1
        return count
    except FileExistsError:
        error_count +=1
        fn_no_ext = os.path.splitext(file_name)[0]
        if mode == '1':
            new_name_2 = folder + fn_no_ext[0:int(val)] + '(' + str(error_count) + ')' + '.txt'
        elif mode == '2':
            length = len(fn_no_ext)
            new_name_2 = folder + fn_no_ext[- int(val):length] + '(' + str(error_count) + ')' + '.txt'
        name_ask = input('The file ' + new_name + ' already exists, do you want to rename it as ' + new_name_2 + '? (Y/N): ')
        if name_ask == 'Y' or name_ask == 'y':
            # Call rename function
            f_rename_2(old_name, new_name_2, val, mode, count, error_count)
            return count
        elif name_ask == 'N' or name_ask == 'n':
            return count
        else:
            print('Wrong input. Program will exit in 5 seconds to prevent any further confusion!')
            time.sleep(5)
            exit()
    except :
        print('Something went wrong with the file ' + old_name + '!')


folder_input = ''
while True:
    # Making a flag variable to prevent the program to run if the folder path is not correct.
    flag = 0
    # Making a variable that will be used to name each file.
    count = 1
    # Making a counter for alternative file_names.
    error_count = 1
    
    if folder_input == '':
        # Calls function to select the desired folder.
        folder, folder_input = access_folder()
        print('Your Folder : ' + str(folder_input) + '\n')
        
    else :
        ask_par = input('Do you want to rename files in a different folder? (Y/N):')
        if ask_par == 'Y' or ask_par == 'y':
                # Calls function to select the desired folder.
                folder, folder_input = access_folder()
                print('Your Folder : ' + str(folder_input) + '\n')
        elif ask_par == 'N' or ask_par == 'n':
            break
        else:
            print('Something went wrong. Please type again your answer! \n')
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
                
                # Calls Rename function.
                count = f_rename(old_name, new_name, count, error_count)
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

                    # Calls Rename function.
                    count = f_rename_2(old_name, new_name, val, mode, count, error_count)
                    
                # Prints a sentence for the user, that the operation was successful.
                print('All ' + str(count - 1) + ' files are renamed.')
            except Exception as e:
                print(e)
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

                    # Calls Rename function.
                    count = f_rename_2(old_name, new_name, val, mode, count, error_count)
                    
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
