# Rate Limit

## Overview
This repository explores the implementation of a custom rate limit handle via middleware.

## Requirements
- Azure subscription for deploying Azure Cosmos DB for MongoDB vCore.
- Python environment with FastAPI installed.

## Usage
1. Follow the steps provided in the README file.

## Steps
1. Create FastAPI and write a logic to handle rate limit.
2. Follow the setup instructions provided in the README file.

## Quickstart

We leverage Python's [virtual environments](https://docs.python.org/3/tutorial/venv.html) (`venv`) to isolate dependencies, ensuring there are no conflicts between across Python installations. As such, the first thing you need to do is install and activate a virtual environment.

In MacOS Terminal:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

In Windows PowerShell:

```sh
python3 -m venv .venv
.venv\Scripts\Activate
```

## Code Hygene

To maintain code quality and consistency, we use Black as a formatter and Flake8 as a linter. For an improved developer experience, we highly recommend installing the corresponding Visual Studio Code extensions. If you prefer to run these tools manually, refer to the commands below.

On MacOS Terminal:

```sh
black . && isort --profile black . && flake8 .
```

On Windows PowerShell:

```sh
black .; if ($?) { isort --profile black . }; if ($?) { flake8 . }
```
