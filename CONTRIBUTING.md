# Contributing to SMTP Tester

Thank you for your interest in contributing to SMTP Tester! We welcome contributions from everyone, whether you're fixing bugs, adding features, improving documentation, or suggesting ideas. This guide will help you get started.

## Getting Started

1. **Fork the Repository**:
   - Click the "Fork" button on the [GitHub repository](https://github.com/Mrv3n0m666/Smtp-Webtester).

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/yourusername/Smtp-Webtester.git
   cd Smtp-Webtester
   ```

3. **Set Up the Environment**:
   - Ensure Python 3.6+ is installed.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file with your OpenAI API key (see `.env.example`).

4. **Run the Application**:
   ```bash
   python smtpWEBtester.py
   ```
   - Test at `http://localhost:5000`.

## How to Contribute

1. **Find an Issue**:
   - Check the [Issues](https://github.com/Mrv3n0m666/Smtp-Webtester/issues) page for tasks labeled `good first issue` or `help wanted`.
   - If you have a new idea, open an issue to discuss it first.

2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   - Use descriptive branch names (e.g., `fix/email-validation`, `feature/add-test-history`).

3. **Make Changes**:
   - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
   - Keep HTML/CSS consistent with `templates/index.html`.
   - Update documentation (e.g., `README.md`) if needed.

4. **Test Your Changes**:
   - Run the app locally to verify functionality.
   - Add tests if applicable (we plan to add a `pytest` suite soon).

5. **Commit Changes**:
   ```bash
   git commit -m "Add your descriptive commit message"
   ```
   - Write clear, concise commit messages (e.g., "Add email validation with email-validator").

6. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**:
   - Go to the [original repository](https://github.com/Mrv3n0m666/Smtp-Webtester).
   - Click "New Pull Request" and select your branch.
   - Provide a detailed description of your changes, referencing related issues (e.g., "Closes #123").

## Contribution Guidelines

- **Code Style**: Adhere to PEP 8 for Python and maintain consistent formatting in HTML/CSS.
- **Scope**: For major changes, open an issue first to discuss with maintainers.
- **Testing**: Ensure your changes don't break existing functionality. Automated tests are coming soon!
- **Documentation**: Update `README.md` or other docs if you add features or change usage.
- **License**: By contributing, you agree your contributions are licensed under the MIT License.

## Code of Conduct
We follow the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and inclusive in all interactions.

## Questions?
If you're unsure about anything, open an issue or contact [Mrv3n0m666](mailto:testceklow123@hotmail.com). We're here to help!