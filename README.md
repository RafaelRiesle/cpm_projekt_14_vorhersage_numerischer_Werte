# Python Project Template (uv + `src/` Layout)

This repository is a **Python project template** using **uv** for dependency management and virtual environments. It follows the recommended **`src/` layout** for clean, maintainable, and scalable Python packaging.

---

# Core Concept

The project is built around two key files.

## `pyproject.toml`

Defines the **desired project configuration**, including:

* Project metadata (name, version, description)
* Runtime dependencies
* Development dependency groups
* Build system configuration

Example:

```toml
[project]
name = "my_project"
version = "0.1.0"
requires-python = ">=3.11"

dependencies = [
    "requests",
]

[dependency-groups]
dev = [
    "pytest",
    "ruff",
]
```

---

## `uv.lock`

Contains the **exact resolved versions of all dependencies**.

This ensures:

* Reproducible installations
* Consistent environments across developers and CI
* Predictable dependency resolution
* No unexpected version conflicts

Do **not** edit this file manually. It is fully managed by `uv`.

---

# Installation

## Install `uv`

### Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternatively:

```bash
pip install uv
```

Verify the installation:

```bash
uv --version
```

---

# Set Up the Project

Run the following commands from the **project root directory**:

```bash
uv venv
uv sync
```

This will:

* Create a virtual environment (`.venv`)
* Install all project dependencies
* Create or update `uv.lock` when dependency resolution changes

---

# Virtual Environment

Activating the virtual environment is optional when using `uv run`, as `uv` automatically executes commands inside the project's environment.

If you want to activate it manually:

## Linux / macOS

```bash
source .venv/bin/activate
```

## Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

---

# Project Structure

```text
.
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── .env
├── .env.template
├── README.md
├── pyproject.toml
├── uv.lock
└── .venv/
```

---

# Key Rules

* `pyproject.toml` defines the desired project configuration.
* `uv.lock` defines the exact installed dependency versions.
* Never edit `uv.lock` manually.
* Store environment-specific configuration in `.env` and provide a `.env.template` with the required variables.
* Never commit `.env` to version control.
* Always run project commands from the repository root.

---

# Typical Workflow

## uv Workflow

```bash
uv venv                              # Create a virtual environment
uv sync                              # Install or synchronize dependencies

uv run pre-commit install            # Install Git pre-commit hooks

uv add <package>                     # Add a runtime dependency
uv add --dev <package>               # Add a development dependency

uv sync --upgrade                    # Upgrade dependencies within configured constraints

uv run python -m my_project.main     # Run the application
uv run pytest                        # Run all tests
```

## Ruff Workflow

```bash
uv run ruff format .                 # Format code

uv run ruff check .                  # Run linting
uv run ruff check . --fix            # Automatically fix lint issues

uv run ruff check . --select I --fix # Fix import sorting only
```

## Testing Workflow

```bash
uv run pytest                        # Run all tests
uv run pytest tests/test_main.py     # Run a specific test file
uv run pytest -k "test_name"         # Run matching tests
```

---

# Makefile

To facilitate the use of the template, we include a makefile developped by LDC. 
Makefiles are used to trigger workflows via the terminal and enable triggering complicated console commands.

The included makefile provides the following command: 
```bash
make setup
```

This will 
* verify uv installation
* install the python version specified in .python-version
* set the project name in pyproject.toml to the folder-name
* install project dependencies via `uv sync` 
* setup pre-commit
* create a .env file for you

## 2. Install make

To get started with make, request installation of make for windows via an it ticket.
There is different ways to install it: 
```bash
winget install GnuWin32.Make
```
https://gnuwin32.sourceforge.net/packages/make.htm

## 3. Make sure git bash is on your PATH

Since this makefile uses bash syntax, make sure to include an installation of bash in your path (typically via git-bash).
A typical location would be C:\Users\testuser\AppData\Local\Programs\Git\bin or C:\Program Files\Git\bin

---
