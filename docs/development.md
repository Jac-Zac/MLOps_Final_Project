# Development Guidelines

This document outlines guidelines for contributing to the **PickaFilm** project, code standards, and instructions for running tests locally.

## Contributing

We welcome contributions to improve **PickaFilm**! To get started:

1. **Fork the Repository:**  
   Fork the project on GitHub and clone your fork locally.

2. **Create a Branch:**  
   Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes:**  
   Implement your changes following the coding standards below.

4. **Submit a Pull Request (PR):**  
   Once your changes are ready, submit a PR with a clear description of your changes and references to any related issues.

## Code Standards

- **Python Version:**  
  We use Python 3.12. Ensure your development environment uses this version.

- **Formatting:**  
  Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python coding style. Tools like `flake8` or `black` can help maintain consistency.

- **Docstrings:**  
  Include docstrings for all public functions and modules to improve code readability and maintainability.

- **Testing:**  
  We use `pytest` for testing. Add tests for any new features and ensure that all tests pass before submitting a PR.

## Running Tests Locally

Before submitting a PR, verify that all tests pass locally:

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests:**
   ```bash
   pytest
   ```

## Development Environment Setup

1. **Clone the Repository:**

   ```bash
   git https://github.com/Jac-Zac/PickaFilm
   cd PickaFilm
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv .env
   source .env/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   > You should add your API key inside `.streamlit/secrets.toml`

   ```bash
   streamlit run src/app.py
   ```

5. **Run tests:**

   > From the root of the directory you can run all of the tests

   ```bash
   pytest tests/test_app.py
   ```

   Happy coding!
