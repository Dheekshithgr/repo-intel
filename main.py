from git import Repo
import tempfile
from pathlib import Path
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


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
        ".gitignore",
        "package.json",
        "manage.py"
    ]

    found_directories = []
    found_files = []

    file_count = 0
    directory_count = 0

    for item in project_path.rglob("*"):

        if ".git" in item.parts:
            continue

        if item.is_dir():

            directory_count += 1

            if item.name in important_directories:
                if item.name not in found_directories:
                    found_directories.append(item.name)

        elif item.is_file():

            file_count += 1

            if item.name in important_files:
                if item.name not in found_files:
                    found_files.append(item.name)

    return {
        "files": file_count,
        "directories": directory_count,
        "important_directories": found_directories,
        "important_files": found_files
    }


def detect_technologies(repository):

    technologies = []

    important_files = repository["important_files"]
    dependencies = repository["dependencies"]

    if "requirements.txt" in important_files:
        technologies.append("Python")

    if "pyproject.toml" in important_files:
        if "Python" not in technologies:
            technologies.append("Python")

    if "package.json" in important_files:
        technologies.append("Node.js")

    if "Dockerfile" in important_files:
        technologies.append("Docker")

    if "manage.py" in important_files:
        technologies.append("Django")

    if "django" in dependencies:
        if "Django" not in technologies:
            technologies.append("Django")

    if "flask" in dependencies:
        technologies.append("Flask")

    if "fastapi" in dependencies:
        technologies.append("FastAPI")

    return technologies


def analyze_git(project_path):

    repo = Repo(project_path)

    branch = repo.active_branch.name

    commits = list(repo.iter_commits())

    commit_count = len(commits)

    latest_commit = repo.head.commit

    git_info = {
        "branch": branch,
        "commit_count": commit_count,
        "latest_commit": {
            "message": latest_commit.message.strip(),
            "author": latest_commit.author.name,
            "date": latest_commit.committed_datetime
        }
    }

    return git_info


def get_github_info(source):

    source = source.rstrip("/")

    if source.endswith(".git"):
        source = source[:-4]

    parts = source.split("/")

    owner = parts[-2]
    repository_name = parts[-1]

    api_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repository_name}"
    )

    try:

        with urlopen(api_url) as response:
            data = json.load(response)

    except HTTPError as e:
        print("Error: Could not access GitHub repository metadata.")
        print("Reason:", e)
        return None

    except URLError as e:
        print("Error: Could not connect to GitHub API.")
        print("Reason:", e)
        return None

    github_info = {
        "owner": data["owner"]["login"],
        "name": data["name"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "topics": data["topics"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"]
    }

    return github_info


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

        git_info = analyze_git(project_path)

        github_info = get_github_info(source)

        repository = {
            "files": structure["files"],
            "directories": structure["directories"],
            "important_directories": structure["important_directories"],
            "important_files": structure["important_files"],
            "languages": [],
            "dependencies": {},
            "technologies": [],
            "readme": None,
            "git": git_info,
            "github": github_info
        }

        programming_languages = {
            ".py": "Python",
            ".js": "JavaScript",
            ".java": "Java",
            ".cpp": "C++",
            ".c": "C"
        }

        for item in project_path.rglob("*"):

            if ".git" in item.parts:
                continue

            if item.is_file():

                extension = item.suffix

                language = detect_language(
                    extension,
                    programming_languages
                )

                if language and language not in repository["languages"]:
                    repository["languages"].append(language)

                if item.name == "README.md":

                    repository["readme"] = read_readme(item)

                elif item.name == "requirements.txt":

                    requirements_content = item.read_text(
                        encoding="utf-8"
                    )

                    repository["dependencies"] = parse_dependencies(
                        requirements_content
                    )

        repository["technologies"] = detect_technologies(repository)

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
    print("Technologies:", repository["technologies"])

    if repository["readme"] is not None:
        print("README: Found")
    else:
        print("README: Not Found")

    print("\nGit Information")
    print("---------------")

    print("Current Branch:", repository["git"]["branch"])
    print("Total Commits:", repository["git"]["commit_count"])

    print(
        "Latest Commit Message:",
        repository["git"]["latest_commit"]["message"]
    )

    print(
        "Latest Commit Author:",
        repository["git"]["latest_commit"]["author"]
    )

    print(
        "Latest Commit Date:",
        repository["git"]["latest_commit"]["date"]
    )

    if repository["github"] is not None:

        print("\nGitHub Information")
        print("------------------")

        print("Owner:", repository["github"]["owner"])
        print("Repository:", repository["github"]["name"])
        print("Description:", repository["github"]["description"])
        print("Stars:", repository["github"]["stars"])
        print("Forks:", repository["github"]["forks"])
        print("Open Issues:", repository["github"]["open_issues"])
        print("Topics:", repository["github"]["topics"])
        print("Created:", repository["github"]["created_at"])
        print("Last Updated:", repository["github"]["updated_at"])


if __name__ == "__main__":
    main()