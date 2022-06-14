import os
import time
import shutil
import datetime
from tkinter import *
from tkinter import filedialog

def access_folder():
    # Pointing root to Tk() to use it as Tk() in program.
    access_window = Toplevel()

    # Hides small tkinter window.
    access_window.withdraw()

    # Opened windows will be active above all windows despite selection.
    access_window.attributes('-topmost', True)

    # Returns opened path as str.
    folder_input = filedialog.askdirectory(initialdir='../', title='Select a folder')

    # Making the path relative, so it can be accessed.
    #folder = folder_input + '\\'

    # Creating and puting on the root window the selected path
    global Entry_field
    Entry_field = Entry(Folder_frame, width = 70, borderwidth = 2)
    Entry_field.insert(0,folder_input)
    Entry_field.grid(row = 0, column = 1, columnspan = 2,  padx = 10, pady = 10)

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


def rename_b(folder_input,mode,n):
    # Making a flag variable to prevent the program to run if the folder path is not correct.
    flag = 0
    # Making a variable that will be used to name each file.
    count = 1
    # Making a counter for alternative file names.
    error_count = 1
    # Making a European date format to name the new folder.
    date = datetime.datetime.now().strftime("%d-%m-%y")
    # Making the path relative, so it can be accessed.
    global folder
    folder = folder_input + '\\'

##    Ask_dst_f = input('Do you want to create a new folder with the renamed files? (Y/N) :')
##    if Ask_dst_f == 'Y' or Ask_dst_f == 'y':
##        # Call create_folder fanction to make a new folder
##        folder = create_folder()
##    else:
##        print('\n !!!!! NO EXTRA FOLDER WILL BE MADE. !!!!! \n')

    mode = mode
    if mode == 0:
        # Loop for each file in the selected folder.
        for file_name in os.listdir(folder):
            if file_name[-4:] == '.txt' :
                old_name = folder + file_name
                new_name = folder + str(count) + '.txt'
            
            # Calls Rename function.
            count = f_rename(old_name, new_name, count, error_count)
        # Prints a sentence for the user, that the operation was successful.
        print('All ' + str(count - 1) + ' files are renamed.')
        print('----------------------------------------------------------------')
        print('\n')  
    elif mode == 1:
        try:
            # Loop for each file in the selected folder.
            for file_name in os.listdir(folder):

                old_name = folder + file_name
                # Creating a new file name without the extension.
                fn_no_ext = os.path.splitext(file_name)[0]
                # Creating a new name for the file keeping only the desired amount of characters.
                new_name = folder + fn_no_ext[0:int(n)] + '.txt'

                # Calls Rename function.
                count = f_rename_2(old_name, new_name, n, mode, count, error_count)
                
            # Prints a sentence for the user, that the operation was successful.
            print('All ' + str(count - 1) + ' files are renamed.')
        except:
            print('An error occured! Please try again.')
        print('----------------------------------------------------------------')
        print('\n')
    elif mode == 2:
        try:
            val = input('Please insert the amount of characters you want to keep: ')
            # Loop for each file in the selected folder.
            for file_name in os.listdir(folder):

                old_name = folder + file_name
                # Creating a new file name without the extension.
                fn_no_ext = os.path.splitext(file_name)[0]
                length = len(fn_no_ext)
                # Creating a new name for the file keeping only the desired amount of characters.
                new_name = folder + fn_no_ext[- int(n):length] + '.txt'

                # Calls Rename function.
                count = f_rename_2(old_name, new_name, n, mode, count, error_count)
                
            # Prints a sentence for the user, that the operation was successful.
            print('All ' + str(count - 1) + ' files are renamed.')
        except:
            print('An error occured! Please try again.')
        print('----------------------------------------------------------------')
        print('\n')

    print(folder_input,mode,n) 

root = Tk()

# Creating frames in the tk window
Folder_frame = LabelFrame(root, text = "Folder", padx = 10, pady = 10)
Modes_frame = LabelFrame(root, text = "Mode", padx = 10, pady = 10)

# Renaming the title of the tk window to "Rename program"
root.title("Rename program")

# Create Labels
Label1 = Label(Folder_frame, text = "Your folder:")
Hint = Label(Folder_frame, text = "Click the Browse button to choose a folder", fg = 'red')
Hint_2 = Label(Modes_frame, text = "*Please type the amount of characters you want to keep in the box above", fg = 'red')

# Create input/output fields
Entry_field = Entry(Folder_frame, width = 70, borderwidth = 2, state = DISABLED)
N_char = Entry(Modes_frame, width = 5, borderwidth = 2)

# Create clickable buttons
Folder_Button = Button(Folder_frame, text="Browse", command = access_folder)
Rename_Button = Button(root, text="RENAME", padx = 10, pady = 3, command = lambda: rename_b(Entry_field.get(),mode.get(),N_char.get()))
Exit_Button = Button(root, text="EXIT", command=root.quit, padx = 10, pady = 3)

# Create Checkbuttons
Copy_b = Checkbutton (Folder_frame, text="Create a new folder with the renamed files", padx = 10, pady = 10)

# Create Radio butons to select mode and put it in the Modes frame
MODES = [
    ("Ascending Order",0),
    ("Keep First n characters *",1),
    ("Keep Last n characters *",2),
    ]

mode = IntVar()
mode.set(0)

for text, value in MODES:
    Radiobutton(Modes_frame, text = text, variable = mode, value = value).pack(anchor = W)
    
# Put Frames on the tk window
Folder_frame.pack(fill="both", expand="yes", padx = 10, pady = 2)
Modes_frame.pack(fill="both", expand="yes", padx = 10, pady = 10)

# Put Labels on the grid of the Folder frame
Label1.grid(row = 0, column = 0)
Hint.grid(row = 1, column = 1, columnspan = 2)
Hint_2.pack(side = BOTTOM)

# Put input/output fields on the tk window
Entry_field.grid(row = 0, column = 1, columnspan = 2,  padx = 10, pady = 10)
N_char.pack(pady = 10)

# Put Buttons on the tk window
Folder_Button.grid(row = 0, column = 3)
Rename_Button.pack(expand = "yes", fill = "both", padx = 10, pady = 5)
Exit_Button.pack(side = RIGHT, padx = 10, pady = 2)

# Put Checkbuttons on the grid of the Folder frame
Copy_b.grid(row = 2, column = 0, columnspan = 2)


root.mainloop()
