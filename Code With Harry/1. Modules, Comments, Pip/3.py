"""
Purpose: To perform various task on directories using os module
Author: Anurag Yadav
Created: 27-07-2025
Language: Python (3.11.9)
Library: os (built-in)
Status: Final
"""
import os

# To get the location of the current working directory
cwd = os.getcwd() 
print("Current working directory:", cwd)
print()


# To Change the Current working directory to one level up
def current_path(label): 
    print(f"Current working directory {label}:") 
    print(os.getcwd()) 
    print() 

current_path("before") # Print the current working directory before changing it
os.chdir('../')  #(../..) means two level up and so on
current_path("After") # Print the new working directory after the change


# To create a new directory inside a specified parent path
directory = "new_file"
parent_dir = r"C:\code_purgatory\DS_AIML\Code With Harry\1. Modules, Comments, Pip"

path = os.path.join(parent_dir, directory) 
os.mkdir(path)
print(f"directory '{directory}' created")  


# List all files and directories in the current directory
files_and_directories = os.listdir(cwd)
print("\nFiles and directories:")
for item in files_and_directories:
    print(item)


# Deleting a directory
remove_dir = "new_file"
location = r"C:\code_purgatory\DS_AIML\Code With Harry\1. Modules, Comments, Pip"
path = os.path.join(location, remove_dir)
os.rmdir(path) # to remove a directory
print(f"\ndirectory '{remove_dir}' deleted")
# os.remove(path) To remove a file


#  Change to a specific directory. for eg: Code With Harry\2. Variables & Datatype
target_directory = r"C:\code_purgatory\DS_AIML\Code With Harry\2. Variables & Datatype"
print("\nThe Current working directory brfore changing:", cwd )
os.chdir(target_directory)
print(f"Changed Directory to: {os.getcwd()}")


