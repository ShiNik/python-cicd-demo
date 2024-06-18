[![Python 3.12.3](https://img.shields.io/badge/python-3.12.3-blue.svg)](https://www.python.org/downloads/release/python-3123/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Coverage](coverage.svg)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/orange?icon=dependabot)](https://dependabot.com/)
[![Actions status](https://github.com/astral-sh/ruff/workflows/CI/badge.svg)](https://github.com/ShiNik/python-cicd-demo/actions)
[![image](https://img.shields.io/pypi/l/ruff.svg)](https://github.com/ShiNik/python-cicd-demo/blob/main/LICENSE)


## Step 1: Install python:
sudo apt-get install python3.11.0

## Step 2: install poetry:
curl -sSL https://install.python-poetry.org | python3 -

## Step 3: Set Up the Virtual Environment
1. Create a virtual environment by typing: `poetry install`
2. poetry run pre-commit install --hook-type commit-msg

## Step 4: Install terraform
https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli

# run pre-commit hook
by typing: `pre-commit run --all-files`

# coverage: Run pytest test coverage
```
poetry run coverage run && poetry run coverage report && poetry run coverage xml && poetry run coverage-badge -f -o coverage.svg
```

# How to run terraform:
- terraform init
- terraform plan
- terraform apply
- terraform  destroy
