from git import Repo
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as temp_dir:

    source = input("\nEnter any GitHub URL: ")

    Repo.clone_from(source, temp_dir)

    project_path = Path(temp_dir)

    file_count = 0
    dir_count = 0

    repository = {}
    dependencies = {}
    languages = []

    programming_languages = {
        ".py": "Python",
        ".js": "JavaScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C"
    }

    for item in project_path.rglob("*"):

        if ".git" not in item.parts:

            if item.is_file():

                file_count += 1

                extension = item.suffix

                if extension in programming_languages:
                    language = programming_languages[extension]

                    if language not in languages:
                        languages.append(language)

                if item.name == "README.md":

                    content = item.read_text()
                    repository["readme"] = content

                elif item.name == "requirements.txt":

                    requirements_content = item.read_text()
                    lines = requirements_content.splitlines()

                    for line in lines:

                        separators = ["==", ">=", "<=", "~=", "!="]
                        found = False

                        for sep in separators:

                            if sep in line:

                                parts = line.split(sep)

                                dependencies[parts[0].strip()] = parts[1].strip()

                                found = True
                                break

                        if not found:
                            dependencies[line.strip()] = "Not specified"

            elif item.is_dir():

                dir_count += 1

    repository["files"] = file_count
    repository["directories"] = dir_count
    repository["languages"] = languages
    repository["dependencies"] = dependencies

    print("\nRepository Profile")
    print("------------------")

    print("Files:", repository["files"])
    print("Directories:", repository["directories"])
    print("Languages:", repository["languages"])
    print("Dependencies:", repository["dependencies"])

    if "readme" in repository:
        print("README: Found")