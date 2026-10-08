ifeq ($(OS),Windows_NT)
    BASH_PATH := $(shell where bash 2>nul)
    ifeq ($(BASH_PATH),)
        $(error bash not found. make sure git bash is on your PATH.)
    endif
    SHELL := bash
    .SHELLFLAGS := -eu -o pipefail -c
endif

PYTHON_VERSION := $(shell cat .python-version)

.PHONY: setup check-requirements install-python set-project-name install-dependencies install-hooks create-env update-pyproject-python

setup: check-requirements install-python update-pyproject-python set-project-name install-dependencies install-hooks create-env

check-requirements:
	@echo "Checking uv installation..."
	@command -v uv >/dev/null 2>&1 || { echo >&2 "Error: uv is not installed. See https://docs.astral.sh/uv/getting-started/installation/"; exit 1; }
	
install-python:
	@echo "Installing Python version $(PYTHON_VERSION)..."
	uv python --system-certs install $(PYTHON_VERSION)

install-dependencies:
	@echo "Installing dependencies..."
	uv sync

install-hooks:
	@echo "Setting up pre-commit hooks..."
	uv run pre-commit install

create-env:
	@if [ -f .env ]; then \
		echo ".env already exists"; \
	elif [ -f .env.template ]; then \
		echo "Creating .env from .env.template..."; \
		cp .env.template .env; \
	else \
		echo "Warning: .env.template not found."; \
	fi

set-project-name:
	@project_name=$$(basename "$$(pwd)"); \
	echo "Setting project name in pyproject.toml to $$project_name..."; \
	if [ ! -f pyproject.toml ]; then \
		echo "Error: pyproject.toml not found!"; \
		exit 1; \
	fi; \
	if grep -qE '^[[:space:]]*name[[:space:]]*=' pyproject.toml; then \
		sed -i.bak -E "s/^[[:space:]]*name[[:space:]]*=.*/name = \"$$project_name\"/" pyproject.toml; \
	else \
		if ! grep -qE '^\[project\]' pyproject.toml; then \
			echo "[project]" >> pyproject.toml; \
		fi; \
		sed -i.bak -E "/^\[project\]/a name = \"$$project_name\"" pyproject.toml; \
	fi; \
	rm -f pyproject.toml.bak; \
	echo "Project name set to $$project_name"

update-pyproject-python:
	@echo "Updating pyproject.toml Python version to $(PYTHON_VERSION)..."
	@if [ ! -f pyproject.toml ]; then \
		echo "Error: pyproject.toml not found!"; \
		exit 1; \
	fi; \
	python_constraint="==$(PYTHON_VERSION)"; \
	if grep -qE '^[[:space:]]*requires-python[[:space:]]*=' pyproject.toml; then \
		sed -i.bak -E "s|^[[:space:]]*requires-python[[:space:]]*=.*|requires-python = \"$$python_constraint\"|" pyproject.toml; \
	else \
		if ! grep -qE '^\[project\]' pyproject.toml; then \
			echo "[project]" >> pyproject.toml; \
		fi; \
		sed -i.bak -E "/^\[project\]/a requires-python = \"$$python_constraint\"" pyproject.toml; \
	fi; \
	rm -f pyproject.toml.bak; \
	echo "Set Python version to $$python_constraint"
