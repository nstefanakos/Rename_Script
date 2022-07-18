import os
import time
import shutil
import datetime
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def access_folder():
    # Creating a new window on top of the main tk.
    access_window = Toplevel()

    # Hides small tkinter window.
    access_window.withdraw()

    # Opened windows will be active above all windows despite selection.
    access_window.attributes('-topmost', True)

    # Returns opened path as str.
    folder_input = filedialog.askdirectory(initialdir='../', title='Select a folder')

    # Creating and puting on the root window the selected path
    global Entry_field
    Entry_field = Entry(Folder_frame, width = 85, borderwidth = 2)
    Entry_field.insert(0,folder_input)
    Entry_field.grid(row = 0, column = 1, columnspan = 2,  padx = 10, pady = 10)

def create_folder(f_type,f_length):
    # Making a European date format to name the new folder.
    date = datetime.datetime.now().strftime("%d-%m-%y")
    
    access_window = Toplevel()
    access_window.withdraw()
    access_window.attributes('-topmost', True)
    folder_input = filedialog.askdirectory(initialdir='../', title='Select a folder to save the renamed files')
    folder_new = folder_input + '\\Renamed_files' + '(' + date + ')' + '\\'
    
    try:
        os.mkdir(folder_new)
        ask_cont = "yes"
    except:
        ask_cont = messagebox.askquestion("FOLDER EXISTS", "The file you are trying to create already exists!\nIf two files have the same name, the one already in the folder will be overwritten.\nDo you want to continue ?")
    finally:
        if ask_cont == "yes": 
            for file_name in os.listdir(folder):
                if file_name[-f_length:] == f_type :
                    shutil.copy(os.path.join(folder,file_name), os.path.join(folder_new,file_name))
        else:
            folder_new = folder
        messagebox.showinfo("NEW FOLDER", "The renamed files will be located in : "+ folder_new)
    return folder_new

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
        name_ask = messagebox.askquestion("QUESTION","The file " + new_name + " already exists.\nDo you want to rename it as " + new_name_2 + "?")

        if name_ask == "yes":
            # Call rename function
            f_rename(old_name, new_name_2, count, error_count)
            return count
        
        elif name_ask == "no":
            return count
        
    except :
        messagebox.showwarning("WARNING", "Something went wrong with the file " + old_name + "!")

def f_rename_2(old_name,new_name,file_name,val,mode,count,error_count):
    try :
        # Rename the file.
        os.rename(old_name, new_name)
        count += 1
        error_count = 1
        return count

    except FileExistsError:
        
        error_count +=1
        fn_no_ext = os.path.splitext(file_name)[0]

        if mode == 1:
            new_name_2 = folder + fn_no_ext[0:int(val)] + '(' + str(error_count) + ')' + '.txt'
        elif mode == 2:
            length = len(fn_no_ext)
            new_name_2 = folder + fn_no_ext[- int(val):length] + '(' + str(error_count) + ')' + '.txt'

        name_ask = messagebox.askquestion("QUESTION","The file " + new_name + " already exists.\nDo you want to rename it as " + new_name_2 + "?")
        if name_ask == "yes":
            # Call rename function
            f_rename_2(old_name, new_name_2, file_name, val, mode, count, error_count)
            return count
        elif name_ask == "no":
            return count
        
    except :
        messagebox.showwarning("WARNING", "Something went wrong with the file " + old_name + "!")

def rename_b(folder_input,cus_name,f_type,Copy,mode,file_type,n):
    # Making a flag variable to prevent the program to run if the folder path is not correct.
    flag = 0
    # Making a variable that will be used to name each file.
    count = 1
    # Making a counter for alternative file names.
    error_count = 1
    # Making the path relative, so it can be accessed.
    global folder
    folder = folder_input + '\\'

    if file_type == 0:
        f_type = '.txt'
        f_length = len(f_type)
    elif file_type == 1:
        f_type = '.jpg'
        f_length = len(f_type)
    elif file_type == 2:
        f_type = '.png'
        f_length = len(f_type)
    elif file_type == 3:
        f_type = '.pdf'
        f_length = len(f_type)
    elif file_type == 4:
        f_length = len(f_type)

    if folder_input == "":
        messagebox.showwarning("WARNING", "You haven't selected a folder!")
        
    else:

        if Copy == 1:
            # Call create_folder fanction to make a new folder
            folder = create_folder(f_type, f_length)
        
        else:
            messagebox.showinfo("NO NEW FOLDER", "The renamed files will remain in their current location.")
        
        if mode == 0:
            try:
                # Loop for each file in the selected folder.
                for file_name in os.listdir(folder):
                    if file_name[-f_length:] == f_type :
                        old_name = folder + file_name
                        new_name = folder + str(count) + f_type
                    
                        # Calls Rename function.
                        count = f_rename(old_name, new_name, count, error_count)
                    
                # Prints a message for the user, that the operation was successful.
                messagebox.showinfo("SUCCESS", "All " + str(count - 1) + " files are renamed.")
            except :
                messagebox.showerror("ERROR", "An error occured! Please try again.")
                
        elif mode == 1:
            try:
                # Loop for each file in the selected folder.
                for file_name in os.listdir(folder):
                    if file_name[-f_length:] == f_type :
                        old_name = folder + file_name
                        
                        # Creating a new file name without the extension.
                        fn_no_ext = os.path.splitext(file_name)[0]
                        
                        # Creating a new name for the file keeping only the desired amount of characters.
                        new_name = folder + fn_no_ext[0:int(n)] + f_type

                        # Calls Rename function.
                        count = f_rename_2(old_name, new_name, file_name, n, mode, count, error_count)
                    
                # Prints a message for the user, that the operation was successful.
                messagebox.showinfo("SUCCESS", "All " + str(count - 1) + " files are renamed.")
            except :
                messagebox.showerror("ERROR", "An error occured! Please try again.")

        elif mode == 2:
            try:
                # Loop for each file in the selected folder.
                for file_name in os.listdir(folder):
                    if file_name[-f_length:] == f_type :
                        old_name = folder + file_name
                        
                        # Creating a new file name without the extension.
                        fn_no_ext = os.path.splitext(file_name)[0]
                        length = len(fn_no_ext)
                        
                        # Creating a new name for the file keeping only the desired amount of characters.
                        new_name = folder + fn_no_ext[- int(n):length] + f_type

                        # Calls Rename function.
                        count = f_rename_2(old_name, new_name, file_name, n, mode, count, error_count)
                    
                # Prints a message for the user, that the operation was successful.
                messagebox.showinfo("SUCCESS", "All " + str(count - 1) + " files are renamed.")
            except :
                messagebox.showerror("ERROR", "An error occured! Please try again.")
                
        elif mode == 3:
            try:
                # Loop for each file in the selected folder.
                for file_name in os.listdir(folder):
                    if file_name[-f_length:] == f_type :
                        old_name = folder + file_name
                        new_name = folder + cus_name + "_" + str(count) + f_type

                        # Calls Rename function.
                        count = f_rename(old_name, new_name, count, error_count)
                    
                # Prints a message for the user, that the operation was successful.
                messagebox.showinfo("SUCCESS", "All " + str(count - 1) + " files are renamed.")
            except :
                messagebox.showerror("ERROR", "An error occured! Please try again.")

root = Tk()

# Creating frames in the tk window
Folder_frame = LabelFrame(root, text = "Folder", padx = 10, pady = 10)
Folder_frame_2 = LabelFrame(Folder_frame, text = "File Type", padx = 20, pady = 10)
Modes_frame = LabelFrame(root, text = "Mode", padx = 10, pady = 10)
Modes_frame_2 = LabelFrame(Modes_frame, relief = FLAT, padx = 10, pady = 10)
Modes_option_frame = LabelFrame(Modes_frame, text = "Options", padx = 10, pady = 10)

# Renaming the title of the tk window to "Rename program"
root.title("Rename program")

# Making the window not resizable to keep the geometry of the widgets
root.resizable(False,False)

# Create Labels
Label1 = Label(Folder_frame, text = "Your folder :")
Label2 = Label(Modes_option_frame, text = "** Number of characters :")
Label3 = Label(Modes_option_frame, text = "*** Custom name :")
Hint = Label(Folder_frame, text = "Click the Browse button to choose a folder", fg = 'red')
Hint_2 = Label(Folder_frame, text = "* You will have to choose where the folder will be saved, after you press the 'RENAME' button", fg = 'red')
Hint_3 = Label(Modes_option_frame, text = "Don't use characters as ( / , \ or - ) for the custom name.", fg = 'red')
Hint_4 = Label(Folder_frame_2, text = "Valid file types are written as '.txt', '.jpg', '.pdf'.", fg = 'red')

# Create input/output fields
Entry_field = Entry(Folder_frame, width = 85, borderwidth = 2, state = DISABLED)
Entry_field_2 = Entry(Modes_option_frame, width = 30, borderwidth = 2)
Entry_field_3 = Entry(Folder_frame_2, width = 10, justify = CENTER, borderwidth = 2)
N_char = Entry(Modes_option_frame, width = 5, justify = CENTER, borderwidth = 2)

# Create clickable buttons
Folder_Button = Button(Folder_frame, text="Browse", command = access_folder)
Rename_Button = Button(root, text="RENAME", padx = 10, pady = 3, command = lambda: rename_b(Entry_field.get(),Entry_field_2.get(),Entry_field_3.get(),Copy.get(),mode.get(),f_type.get(),N_char.get()))
Exit_Button = Button(root, text="EXIT", command=root.quit, padx = 10, pady = 3)

# Create Checkbuttons
Copy = IntVar()
Copy_b = Checkbutton (Folder_frame, text="Create a new folder with the renamed files *", variable = Copy, padx = 10, pady = 10)

# Create Radio butons
TYPES = [
    ("TEXT",0),
    ("JPEG",1),
    ("PNG",2),
    ("PDF",3),
    ("Custom file type :",4)
    ]

f_type = IntVar()
f_type.set(0)

for text, value in TYPES:
    Radiobutton(Folder_frame_2, text = text, variable = f_type, value = value).grid(row = value, column = 0, sticky = W)

MODES = [
    ("Numerical Ascending Order",0),
    ("Keep First n Characters **",1),
    ("Keep Last n Characters **",2),
    ("Custom ***",3)
    ]

mode = IntVar()
mode.set(0)

for text, value in MODES:
    Radiobutton(Modes_frame_2, text = text, variable = mode, value = value).pack(anchor = W)
    
# Put Frames on the tk window
Folder_frame.pack(fill="both", expand="yes", padx = 10, pady = 2)
Folder_frame_2.grid(row = 2, column = 0, columnspan = 2, pady = 10)
Modes_frame.pack(fill="both", expand="yes", padx = 10, pady = 10)
Modes_frame_2.grid(row  = 0, column = 0, padx = 20)
Modes_option_frame.grid(row = 0, column = 1, padx = 10)

# Put Labels on the grid of the Folder frame
Label1.grid(row = 0, column = 0)
Label2.grid(row = 0, column = 0)
Label3.grid(row = 1, column = 0)
Hint.grid(row = 1, column = 1, columnspan = 2)
Hint_2.grid(row = 4, column = 0, columnspan = 4)
Hint_3.grid(row = 2, column = 0, columnspan = 3)
Hint_4.grid(row = 5, column = 0, columnspan = 2)

# Put input/output fields on the tk window
Entry_field.grid(row = 0, column = 1, columnspan = 2,  padx = 10, pady = 10)
Entry_field_2.grid(row = 1, column = 1, columnspan = 2,  padx = 10, pady = 10)
Entry_field_3.grid(row = 4, column = 1, rowspan = 1,  padx = 10, pady = 10)
N_char.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)

# Put Buttons on the tk window
Folder_Button.grid(row = 0, column = 3)
Rename_Button.pack(expand = "yes", fill = "both", padx = 10, pady = 5)
Exit_Button.pack(side = RIGHT, padx = 10, pady = 2)

# Put Checkbuttons on the grid of the Folder frame
Copy_b.grid(row = 3, column = 0, columnspan = 2)


root.mainloop()
