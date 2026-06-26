import os
import shutil # library for moving files and directories

# folder path you want to organize
folder_path = os.getcwd()  # Current working directory #getcwd() returns the current working directory (CWD) of the process. This is the folder from which the script is being run.
 

# file type mappings
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': [ '.js', '.sh', '.bat']
}


#create folders if they don't exist
for folder in file_types.keys(): # folder is the key in the file_types dictionary
    folder_dir = os.path.join(folder_path, folder) # folder_dir is the path to the folder you want to create
    if not os.path.exists(folder_dir):# check if the folder already exists
        os.makedirs(folder_dir) # create the folder if it doesn't exist



# organize files 
for file in os.listdir(folder_path):  # file is one of the files in the folder_path that you want to organize
    file_path = os.path.join(folder_path, file) # get the full path of the file that you want to organize   


    # skip folders
    if os.path.isdir(file_path):
        continue


 #get the file extension
    file_extension = os.path.splitext(file)[1].lower() # splitext() splits the file name into a tuple (root, ext) where ext is the file extension. lower() converts the extension to lowercase.
    #file_extension is a variable that stores the file extension of the current file being processed. It is obtained by splitting the file name into its root and extension using os.path.splitext() and then converting the extension to lowercase using .lower().


    for folder, extensions in file_types.items(): # folder is the key in the file_types dictionary and extensions is the value (list of extensions)    # items()   returns a view object that displays a list of a dictionary's key-value tuple pairs.
  
          if file_extension in extensions: # check if the file extension is in the list of extensions for the current folder
           shutil.move(file_path, os.path.join(folder_path, folder, file)) # move the file to the corresponding folder
            
        
print("Files organized successfully!")  