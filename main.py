import os
import datetime

def delete_old_files(folder_path):
    current_time = datetime.datetime.now()

    # Iterate over all the files and folders in the specified directory
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        # Check if it's a file
        if os.path.isfile(item_path):
            # Get the last modified time of the file
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
    
            time_difference = current_time - modified_time
            if time_difference.days > 30:
                os.remove(item_path)
                print(f"Deleted: {item_path}")
        
        # Check if it's a directory
        elif os.path.isdir(item_path):
            # Recursively call the function for subdirectories
            delete_old_files(item_path)
            
    # After deleting old files, check if the directory is empty and delete it
    if not os.listdir(folder_path):
        os.rmdir(folder_path)
        print(f"Deleted empty directory: {folder_path}")

folder_to_check = r"C:\Users\tobia\Downloads"

delete_old_files(folder_to_check)
