# Alexa-Assist

[![GitHub issues](https://img.shields.io/github/issues/pablosambuco/alexa-assist?logo=github&label=Issues&logoColor=959da5&style=flat-square)](https://github.com/pablosambuco/alexa-assist/issues)
[![Pylint](https://img.shields.io/github/actions/workflow/status/pablosambuco/alexa-assist/pylint.yml?style=flat-square&logo=github&logoColor=959da5&label=PyLint)](https://github.com/pablosambuco/alexa-assist/actions?query=workflow%3APylint)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/pablosambuco/alexa-assist/codeql-analysis.yml?style=flat-square&logo=github&logoColor=959da5&label=CodeQL)](https://github.com/pablosambuco/alexa-assist/actions?query=workflow%3ACodeQL)

[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/pablosambuco/alexa-assist?logo=python&style=flat-square&logoColor=white)](https://www.python.org/)
[![GitHub Pipenv locked dependency version (branch)](https://img.shields.io/github/pipenv/locked/dependency-version/pablosambuco/alexa-assist/fastapi/master?logo=fastapi&style=flat-square&logoColor=white)](https://fastapi.tiangolo.com/) 

[![Raspberry Pi](https://img.shields.io/badge/powered%20by-Raspberry%20Pi-C51A4A.svg?logo=raspberry-pi&style=flat-square)](https://www.raspberrypi.org)

## Description
Alexa-Assist is a Python application leveraging FastAPI to handle POST requests from Alexa skills developed through Amazon's Developer Console (or any other service capable of initiating requests). This application is designed to receive commands from Alexa devices and execute specific programmed actions in response to those commands.

## Requirements
- Python 3.8 or higher
- FastAPI
- Uvicorn (to serve the application)

## Installation

First, clone the repository to your local machine:
```bash
git clone https://github.com/pablosambuco/alexa-assist.git
cd alexa-assist
```

Then, install the dependencies using pip:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use Uvicorn with the following command:
```bash
uvicorn api:APP --reload
```

This will start the server on http://127.0.0.1:8000. The application is now ready to receive and respond to POST requests from Alexa skills.

## Developing Alexa Skills

To integrate with Alexa, you will need to create a skill in Amazon's Developer Console configured to send POST requests to the server where this application is running. Refer to the official Alexa Skills Kit documentation for more details on how to do this.

## Contributing

Contributions are welcome, whether in the form of feature suggestions, bug reports, or pull requests. To contribute:

1. Fork the project
2. Create your Feature Branch °git checkout -b feature/AmazingFeature°
3. Commit your changes °git commit -m 'Add some AmazingFeature'°
4. Push to the Branch °git push origin feature/AmazingFeature°
5. Open a Pull Request

## License

Distributed under the MIT License. See °LICENSE° for more information.

## Contact

Project Link: [https://github.com/pablosambuco/alexa-assist](https://github.com/pablosambuco/alexa-assist)
