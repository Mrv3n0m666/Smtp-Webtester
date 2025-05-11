# SMTP Tester

A Flask-based web application to test SMTP server connections and send test emails. This tool is designed to help developers and system administrators verify SMTP server configurations with a user-friendly interface and chat support.

## Overview

SMTP Tester allows you to:
- Test SMTP server connectivity with various security options (None, SSL, TLS, Auto).
- Send test emails to verify sender and recipient addresses.
- Interact with a chat feature for real-time assistance.
- Validate email addresses before sending.
- Secure form submissions with CSRF protection.
- Configure sensitive settings via `.env` file.

This project is open-source under the MIT License and welcomes contributions from the community.

## Installation and Usage

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Mrv3n0m666/smtp-Webtester.git
   cd smtp-tester
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your OpenAI API key:
   ```text
   OPENAI_API_KEY=sk-proj-your-api-key
   ```
4. Run the application:
   ```bash
   python smtpWEBtester.py
   ```

### Usage
1. Open your browser and navigate to `http://localhost:5000`.
2. Fill in the SMTP server details:
   - **SMTP Host**: e.g., `smtp.example.com`
   - **Port**: Common ports are `465` (SSL) or `587` (TLS)
   - **Security**: Choose `None`, `SSL`, `TLS`, or `Auto`
   - **Username**: Your SMTP username (e.g., `your@email.com`)
   - **Password**: Your SMTP password or API key
   - **Mail From**: Sender email address
   - **Mail To**: Recipient email address
3. Click **Test SMTP** to send a test email.
4. Check the result message for success or error details.
5. Use the chat feature on the right to ask for assistance or troubleshooting tips.

### Notes
- Ensure your SMTP server supports the selected security protocol.
- Email addresses are validated before sending to prevent errors.
- The form is protected against CSRF attacks.
- For production use, configure a secure environment and remove debug mode (`debug=True`).

## Contributing

We welcome contributions to improve SMTP Tester! Follow these steps to contribute:

1. **Fork the Repository**:
   - Click the "Fork" button on the [GitHub repository](https://github.com/Mrv3n0m666/smtp-Webtester).

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/Mrv3n0m666/smtp-Webtester.git
   cd smtp-tester
   ```

3. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**:
   - Implement your feature or bug fix.
   - Ensure code follows PEP 8 style guidelines.
   - Update documentation if necessary (e.g., README.md).

5. **Test Your Changes**:
   - Run the application locally to verify functionality.
   - Add tests if applicable (future test suite planned).

6. **Commit Changes**:
   ```bash
   git commit -m "Add your descriptive commit message"
   ```

7. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**:
   - Go to the [original repository](https://github.com/Mrv3n0m666/smtp-Webtester).
   - Click "New Pull Request" and select your branch.
   - Provide a clear description of your changes and reference any related issues.

### Contribution Guidelines
- **Code Style**: Follow PEP 8 for Python and use consistent HTML/CSS formatting.
- **Issues**: Check the [Issues](https://github.com/Mrv3n0m666/smtp-Webtester/issues) page for tasks or report new bugs/features.
- **Scope**: For major changes, open an issue first to discuss with maintainers.
- **License**: By contributing, you agree that your contributions will be licensed under the MIT License.

## License
MIT License. See [LICENSE](LICENSE) for details.

## Contact
For questions or suggestions, open an issue or contact [Your Name](mailto:your.email@example.com).