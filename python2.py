import os

def list_files_with_size(directory):
    directory = os.path.expanduser(directory)
    
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            
            print(f"{filename}: {file_size} bytes")

home_directory = "~/"
list_files_with_size(home_directory)
