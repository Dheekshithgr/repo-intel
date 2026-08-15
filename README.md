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

### Day 4 — File Type & Language Analysis
- Added file extension detection using `Path.suffix`
- Counted file extensions using dictionaries
- Handled files without extensions
- Added programming language mapping
- Added other file type mapping
- Separated programming languages from other file types
- Added fallback handling for unknown extensions
- Tested with the stock-market-analysis repository

### Day 5 — Important Repository Files
* Created `experiments/scan_repo.py` for repository inspection
* Simplified the scanning logic to focus on repository analysis
* Learned to identify important files using `Path.name`
* Detected `README.md` files
* Read README contents using `Path.read_text()`
* Detected `requirements.txt`
* Read dependency file contents using `Path.read_text()`
* Learned that `requirements.txt` contains package dependencies rather than Python `import` statements
* Understood the difference between repository documentation and dependency declarations
* Completed the basic important-file inspection stage

### Day 6 — Dependency Analysis
* Learned how to split dependency strings using `split()`
* Learned how to split a requirements file into individual lines using `splitlines()`
* Extracted package names and versions from `requirements.txt`
* Handled dependencies with exact versions using `==`
* Added support for version operators:

  * `==`
  * `>=`
  * `<=`
  * `~=`
  * `!=`
* Handled packages without a specified version
* Learned how to use a boolean flag (`found`) to track whether a matching operator was detected
* Built a basic dependency parser for `requirements.txt`
* Completed the basic dependency analysis stage

### Day 7 — Repository Profile
- Learned how to use dictionaries to represent repository information
- Created a structured repository profile
- Stored file and directory counts in the profile
- Stored README content in the profile
- Stored parsed dependencies in the profile
- Stored detected programming languages in the profile
- Used lists to store unique programming languages
- Changed RepoIntel from directly printing information to collecting structured data
- Added a clean repository profile summary
- Successfully built a repository profile from a real GitHub repository