# RepoIntel

RepoIntel is a Python-based tool that scans GitHub repositories and generates a basic repository profile.

## Progress

### Phase 1 — Setup
- Project setup
- Virtual environment
- GitPython configuration
- GitHub repository setup

### Phase 2 — Repository Scanning
- Clone GitHub repositories
- Recursively scan files and directories
- Count files and directories
- Ignore `.git`

### Phase 3 — Repository Analysis
- Detect programming languages
- Detect README
- Parse `requirements.txt`
- Extract dependencies and versions
- Generate repository profile

### Phase 4 — Refactoring & Reliability
- Created reusable functions
- Separated dependency, README, language, and structure analysis
- Moved the analyzer into `main.py`
- Added `main()` as the application entry point
- Added dependency parsing for blank lines and comments
- Added UTF-8 text reading
- Added basic repository cloning error handling
- Added repository structure analysis
- Detect important files and directories
- Count files and directories

### Phase 5 — Technology Detection
- Detect Python projects
- Detect Node.js projects
- Detect Docker usage
- Detect Django projects
- Detect Flask projects
- Detect FastAPI projects
- Analyze repository files and dependencies to identify technologies

### Phase 6 — Git Repository Analysis
- Detect current Git branch
- Count total commits
- Analyze the latest commit
- Extract latest commit message
- Extract commit author
- Extract commit date

## Tech Stack

- Python
- GitPython
- pathlib
- tempfile

## Current Features

- GitHub repository cloning
- File and directory analysis
- Repository structure analysis
- Important file and directory detection
- Language detection
- README detection
- Dependency parsing
- Repository profiling
- Basic error handling
- Technology and framework detection
- Git repository metadata analysis
- Current branch detection
- Commit history analysis

## Future Goals

- Project structure detection
- Framework detection
- GitHub metadata analysis
- Code analysis
- AI-powered repository analysis
- Detailed repository reports