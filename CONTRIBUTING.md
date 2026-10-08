# Contributing Guide

This project follows established Python community standards and internal best practices to ensure readability, maintainability, and consistency across the codebase.

---

## Python Conventions

| Category       | Convention                        | Example                 |
| -------------- | --------------------------------- | ----------------------- |
| File Names     | lowercase with underscores        | `data_loader.py`      |
| Variable Names | `snake_case`                    | `total_count`         |
| Function Names | `snake_case`                    | `load_data()`         |
| Class Names    | `PascalCase`                    | `DataLoader`          |
| Constants      | `UPPER_CASE`                    | `MAX_RETRIES`         |
| Indentation    | 4 spaces                          | –                      |
| Line Length    | max 88 characters (Black)         | –                      |
| Imports        | standard → third‑party → local | –                      |
| Type Hints     | recommended / required            | `def load() -> list:` |
| Docstrings     | module, class, function (PEP 257) | –                      |
| Error Handling | specific exceptions only          | `except ValueError:`  |

Notes:

- Code formatting is enforced using **Black**
- Import order is enforced using **isort**
- Linting may be enforced via **ruff** or **flake8**

---

## Project Structure

This project uses the **src layout** pattern.

```
project-root/
├── src/
│   └── project_name/
│       ├── __init__.py
│       └── module.py
├── tests/
├── pyproject.toml
└── README.md
```

---

## JSON Conventions

JSON files used for configuration or data exchange should follow these rules:

| Rule         | Convention                      |
| ------------ | ------------------------------- |
| Key Naming   | `lowerCamelCase`              |
| Root Element | Prefer an object                |
| Structure    | Predictable, avoid deep nesting |
| Indentation  | 2 spaces                        |
| Comments     | Not allowed (standard JSON)     |

### Example JSON

```json
{
  "userId": 123,
  "name": "Alice",
  "roles": ["admin", "editor"],
  "settings": {
    "theme": "dark"
  }
}
```

---

## Dependency & Environment Management

| Topic                | Convention                        |
| -------------------- | --------------------------------- |
| Tool                 | uv                            |
| Virtual Environments | Managed by uv                 |
| Lock File            | `uv.lock` must be committed |
| Python Version       | Defined in`pyproject.toml`      |


## Commit Message Convention

This project follows **Conventional Commits**.

Format:

```
type: short description
```

| Type     | Usage                    |
| -------- | ------------------------ |
| feat     | New feature              |
| fix      | Bug fix                  |
| chore    | Tooling / setup changes  |
| docs     | Documentation            |
| refactor | Code restructuring       |
| test     | Adding or updating tests |

Example:

```
chore: initial python project template with uv and src layout
```

---

## Summary

- Follow PEP‑based Python conventions
- Use uv for dependency and environment management
- Keep code formatted, typed, and lint-free
- Ensure all contributions align with the defined structure and standards
