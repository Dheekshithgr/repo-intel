from git import Repo
import tempfile
from pathlib import Path

def parse_dependencies(content):

    dependencies = {}

    lines = content.splitlines()

    for line in lines:
        
        if not line.strip() or line.strip().startswith("#"):
            continue

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

    return dependencies

def read_readme(path):
    return path.read_text(encoding="utf-8")

def detect_language(extension, programming_languages):
    if extension in programming_languages:
        return programming_languages[extension]

    return None

def analyze_structure(project_path):

    important_directories = [
        "src",
        "tests",
        "test",
        "docs",
        "config",
        "scripts",
        "data"
    ]
    important_files = [
        "README.md",
        "requirements.txt",
        "pyproject.toml",
        "setup.py",
        "Dockerfile",
        ".gitignore"
    ]

    found_directories = []
    found_files = []
    file_count = 0
    directory_count = 0
    
    for item in project_path.rglob("*"):

        if ".git" in item.parts:
            continue

        if item.is_dir():
            directory_count+=1
            if item.name in important_directories:
                if item.name not in found_directories:
                    found_directories.append(item.name)
        elif item.is_file():
            file_count+=1
            if item.name in important_files:
                if item.name not in found_files:
                    found_files.append(item.name)
    
    return {
        "files": file_count,
        "directories": directory_count,
        "important_directories": found_directories,
        "important_files": found_files
        
    }

def scan_repository(source):

    with tempfile.TemporaryDirectory() as temp_dir:

        try:
            Repo.clone_from(source, temp_dir)
        except Exception as e:
            print("Error: Could not clone the repository.")
            print("Reason:", e)
            return None

        project_path = Path(temp_dir)
        structure = analyze_structure(project_path)

        repository = {
            "files": structure["files"],
            "directories": structure["directories"],
            "languages": [],
            "dependencies": {},
            "readme": None,
            "important_directories": structure["important_directories"],
            "important_files": structure["important_files"]
        }
        repository["important_directories"] = structure["important_directories"]
        repository["important_files"] = structure["important_files"]

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

                    extension = item.suffix

                    if extension in programming_languages:
                        language = detect_language(extension, programming_languages)

                        if language and language not in repository["languages"]:
                            repository["languages"].append(language)

                    if item.name == "README.md":

                        repository["readme"] = read_readme(item)

                    elif item.name == "requirements.txt":

                        requirements_content = item.read_text(encoding="utf-8")
                        repository["dependencies"] = parse_dependencies(requirements_content)
                                        
    return repository


def main():

    source = input("\nEnter any GitHub URL: ")

    repository = scan_repository(source)
    if repository is None:
        return

    print("\nRepository Profile")
    print("------------------")

    print("Files:", repository["files"])
    print("Directories:", repository["directories"])
    print("Important Files:", repository["important_files"])
    print("Important Directories:", repository["important_directories"])
    print("Languages:", repository["languages"])
    print("Dependencies:", repository["dependencies"])

    if repository["readme"] is not None:
        print("README: Found")
    else:
        print("README: Not Found")

if __name__ == "__main__":
    main()