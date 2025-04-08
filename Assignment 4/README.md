<!-- @format -->

# Assignment 4: Spam Classification with `Docker` and Introduction to `Git hooks`.

This project demonstrates how to containerize a Flask-based spam classification app using Docker. It also sets up a basic Continuous Integration (CI) workflow and Git `pre-commit` hooks to ensure code quality.

## Project Structure

Here's a breakdown of the key files and directories:

### 1. [`tests/`](./tests/)

This directory contains automated tests to ensure the Flask API is working correctly within the Docker container.

- [`docker_test.py`](./tests/docker_test.py): This script builds the Docker image, runs the container, and then sends requests to the API to verify that it's behaving as expected.

### 2. [`Dockerfile`](./../Dockerfile)

This `Dockerfile` is used to create a Docker image for a Python application. Here's a breakdown of each instruction:

#### 1. Base Image

```dockerfile
FROM python:3.9-slim
```

- Uses the official Python 3.9 slim image as the base.
- The slim version is smaller than the regular image, containing only minimal packages.

#### 2. Working Directory

```dockerfile
WORKDIR /app
```

- Sets `/app` as the working directory in the container.
- All subsequent commands will be executed from this directory.

#### 3. Copying Application Files

```dockerfile
ARG src="./Assignment 4/"
ARG target="."
COPY ${src} ${target}
```

- Defines two build arguments (`src` and `target`).
- Copies files from the local `./Assignment 4/` directory to the container's `/app` directory.
- The `target="."` means files will be copied to the current working directory (`/app`).

#### 4. Copying Requirements

```dockerfile
COPY requirements.txt .
```

- Copies the `requirements.txt` file from the host to the container's `/app` directory.
- This file typically lists all Python dependencies.

#### 5. Installing Dependencies

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

- Installs Python packages listed in `requirements.txt`.
- The `--no-cache-dir` flag prevents `pip` from caching packages, reducing the image size.

#### 6. Exposing Port

```dockerfile
EXPOSE 5000
```

- Informs Docker that the container listens on port `5000`.
- This is typically used for Flask applications (default port).

#### 7. Running the Application

```dockerfile
CMD ["python", "app.py"]
```

- Specifies the default command to run when the container starts.
- Executes `python app.py` to start the application.

The resulting image will be relatively small due to using `python:3.9-slim`.

### 3. Pre-commit Hook ([`pre-commit`](../.githooks/pre-commit))

#### Pre-commit Hook Overview

The pre-commit hook ensures that all tests pass before allowing a commit. It runs `pytest` in a virtual environment and prevents commits if any tests fail. Below is a summary of the script:

1. **Purpose**:

   - Runs `pytest` to validate the code before committing changes.

2. **Setup**:

   - Ensure the Git hooks path is set using:
     ```sh
     git config core.hooksPath .githooks
     ```

3. **Key Steps**:

   - Checks if a virtual environment (`venv`) exists.
   - Activates the virtual environment based on the operating system.
   - Runs `pytest` using the Python interpreter from the virtual environment.
   - Aborts the commit if any tests fail.

4. **Error Handling**:

   - If the virtual environment is missing, it provides instructions to create one:
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Unix/MacOS
     venv\Scripts\activate     # On Windows
     pip install -r requirements.txt
     ```

5. **Outcome**:
   - If all tests pass, the commit proceeds.
   - If tests fail, the commit is aborted with an error message.

This hook ensures code quality by enforcing that all tests pass before changes are committed.

You need to run `git config core.hooksPath .githooks` to set the hooks path.
