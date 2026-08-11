from git import Repo
import tempfile
from pathlib import Path

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    source = input("Enter the URL: ")

    # Use the temporary directory as the clone destination
    destination = temp_dir

    # Clone the remote repository into the temporary directory
    Repo.clone_from(source, destination)

    print("Cloned successfully")
    print("Repository location:", temp_dir)

    # Convert the directory path into a Path object
    project_path = Path(temp_dir)

    print("Repository contents:")

    file_count=0
    dir_count=0
    # Recursively go through all files and folders
    for item in project_path.rglob("*"):
        # Ignore Git's internal metadata directory
        if ".git" not in item.parts:
            if item.is_file():
                file_count+=1
            elif item.is_dir():
                dir_count += 1
            print(item.name)
            
    print(f"Number of files: {file_count}")
    print(f"Number of directories: {dir_count}")