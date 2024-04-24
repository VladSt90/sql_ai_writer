# AI SQL writer

Generate SQL based on DB context and question about db data

## Setup

This project uses the `llama3` model with `ollama` setup. Follow these steps to set up your environment:

### Clone the Repository

First, ensure you have cloned the repository:

```
git clone [URL to your repository]
cd [repository name]
```

### Setup Ollama

Download and install ollama

### Install Poetry

This project uses [Poetry](https://python-poetry.org/) for managing dependencies. Make sure you have Poetry installed on your system. If you do not have Poetry installed, you can install it with:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Install Dependencies

To install the necessary dependencies, run the following command in the project directory:

```bash
poetry install
```

## Running the Application

To run the application, use the following command:

```bash
poetry run python main.py
```

Ensure you are in the project directory when you run this command.