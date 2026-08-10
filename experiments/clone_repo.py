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

    # Recursively go through all files and folders
    for item in project_path.rglob("*"):
        # Ignore Git's internal metadata directory
        if ".git" not in item.parts:
            print(item.name)
   
