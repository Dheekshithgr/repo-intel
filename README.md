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

## Future Goals

- Project structure detection
- Framework detection
- GitHub metadata analysis
- Code analysis
- AI-powered repository analysis
- Detailed repository reports