from git import Repo
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as temp_dir:

    source = input("\nEnter any GitHub URL: ")

    Repo.clone_from(source, temp_dir)

    project_path = Path(temp_dir)

    file_count = 0
    dir_count = 0

    for item in project_path.rglob("*"):

        if ".git" not in item.parts:

            if item.is_file():

                file_count += 1

                if item.name == "README.md":
                    content = item.read_text()

                    print("\nREADME Found!\n")
                    print(content)
                elif item.name == "requirements.txt":
                    requirements_content = item.read_text()
                    lines = requirements_content.splitlines()
                    for line in lines:
                        separators=["==",">=","<=","~=","!="]
                        found = False
                        for sep in separators:
                            if sep in line:
                                parts=line.split(sep)
                                print(f"Package: {parts[0]}")
                                print(f"Version: {parts[1]}")
                                found = True
                        if not found:
                            print(f"Package: {line.strip()}")
                            print(f"Version: Not specified")
                    print("Requirements file found!")

            elif item.is_dir():
                dir_count += 1

    print(f"\nNumber of files: {file_count}")
    print(f"Number of directories: {dir_count}")