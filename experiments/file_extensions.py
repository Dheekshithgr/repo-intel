from git import Repo
import tempfile
from pathlib import Path

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:

    source = input("\nEnter any GitHub URL: ")

    # Use the temporary directory as the clone destination
    destination = temp_dir

    # Clone the remote repository into the temporary directory
    Repo.clone_from(source, destination)

    print("Cloned successfully\n")
    print("Repository location:", temp_dir)
    print()

    # Convert the directory path into a Path object
    project_path = Path(temp_dir)

    # Dictionary to store extension counts
    extensions = {}

    # Programming language extensions
    programming_languages = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".cs": "C#",
        ".go": "Go",
        ".rs": "Rust",
        ".c": "C"
    }

    # Other common file types
    other_file_types = {
        ".html": "HTML",
        ".css": "CSS",
        ".md": "Markdown",
        ".json": "JSON",
        ".yaml": "YAML",
        ".yml": "YAML"
    }

    # Combine both dictionaries for displaying file types
    file_type_names = {
        **programming_languages,
        **other_file_types
    }

    print("Repository contents:")

    file_count = 0
    dir_count = 0

    # Recursively go through all files and folders
    for item in project_path.rglob("*"):

        # Ignore Git's internal metadata directory
        if ".git" not in item.parts:

            if item.is_file():
                
                file_count += 1

                extension = item.suffix

                # Only count files that have an extension
                if extension:

                    if extension not in extensions:
                        extensions[extension] = 1
                    else:
                        extensions[extension] += 1

            elif item.is_dir():
                dir_count += 1

            print(f"    {item.name}")

    print()

    # Display file extension statistics
    print("File extensions:")

    for extension, count in extensions.items():

        file_type = file_type_names.get(extension, "Unknown")

        print(f"{file_type} ({extension}) -> {count}")

    print()

    # Display programming languages
    print("Programming Languages:")

    for extension in extensions:

        if extension in programming_languages:
            print(programming_languages[extension])

    # Display other file types
    print("\nOther File Types:")

    for extension in extensions:

        if extension in other_file_types:
            print(other_file_types[extension])

    print()

    # Final repository statistics
    print(f"Number of files: {file_count}")
    print(f"Number of directories: {dir_count}")