### Day 1 — Project Setup

- Created the RepoIntel project and GitHub repository
- Set up a Python virtual environment using `venv`
- Installed and configured GitPython
- Verified Git and GitPython installation
- Created the initial project structure
- Added `requirements.txt`
- Added `.gitignore`
- Configured the Git remote for the GitHub repository
- Created the initial `main.py` entry point
- Created an `experiments/` directory for testing and learning components

### Day 2 — Repository Cloning & Scanning
- Learned how to clone GitHub repositories using GitPython
- Used `tempfile.TemporaryDirectory()` to avoid permanently storing cloned repositories
- Used `pathlib.Path` to work with repository paths
- Used `rglob("*")` to recursively scan repository contents
- Learned to identify files and directories using `is_file()` and `is_dir()`
- Excluded `.git` metadata from scanning

### Day 3 — Repository Statistics
- Added recursive file and directory counting
- Counted files using `is_file()`
- Counted directories using `is_dir()`
- Tested scanning on nested repositories
- Tested RepoIntel with a larger ASP.NET repository
- Successfully scanned a repository containing 326 files and 90 directories