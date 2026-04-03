import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar.gz"],
    "Applications": [".exe", ".dmg", ".deb", ".msi"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

def create_folders(base_path):
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(base_path, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def get_unique_filename(folder_path, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder_path, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_filename

def organize_files(base_path):
    create_folders(base_path)
    summary = {folder: 0 for folder in FILE_TYPES.keys()}
    unsorted_files = []

    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)

        if os.path.isfile(file_path):

            moved = False

            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    destination_folder = os.path.join(base_path, folder)
                    unique_filename = get_unique_filename(destination_folder, filename)
                    shutil.move(file_path, os.path.join(destination_folder, unique_filename))
                    
                    summary[folder] += 1
                    moved = True
                    break
            
            if not moved:
                unsorted_files.append(filename)
    
    return summary, unsorted_files

if __name__ == "__main__":
    path = input("Enter the path to organize: ")
    summary, unsorted_files = organize_files(path)
    print("Files have been organized.")
    print("\nSummary of organized files:")
    for folder, count in summary.items():
        print(f"{folder}: {count} files")
    
    if unsorted_files:
        print("\nUnsorted files\n")
        for filename in unsorted_files:
            print(f" - {filename}")