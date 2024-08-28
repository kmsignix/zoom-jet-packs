# Zoom Jet Packs, Powered by SIGNiX
![Zoom-Jet-Packs-Logo-transparent-background-400x400](https://github.com/user-attachments/assets/db329363-cef2-4908-9482-96ee80712bd6)
![SIGNiX (4c) (Custom)](https://github.com/user-attachments/assets/af5bbf18-ee52-41b3-9637-cd28c5537ac4)

## Description
SIGNiX digital signature platform is integrated into a simple Python Flask web application.

This project is provided as a showcase and tutorial for integrating SIGNiX digital signatures
into a lease origination system. While the example is for leasing, the general concepts apply to any use case where
documents are dynamically populated and then signed.

For details on SIGNiX and to get a developer account (required to run this demo), click [here](https://www.signix.com/).

The Python Flask module is used to create a web application, and Jinja templates (included with 
Flask) are used to generate a dynamically-populated lease document in HTML format. HTML documents are converted to PDF using 
pdfkit (which in turn uses wkhtmltopdf, which must be installed). A static PDF containing PDF signature and date fields is also included.

When the user selects "Sign" from the menu, the application creates a transaction containing the
documents and sends it to SIGNiX via the FLEX API. SIGNiX responds with a link / redirection for the lease 
manager to sign the lease document. Once they have signed, SIGNiX invites the lessee to sign via email,
and uses SMS authentication to ensure the signer is as intended.

The code is written to be simple to understand and follow. Transaction, configuration and signer data is statically initialized (in Python / JSON-like 
object structures), so a database is not necessary.

**Text Tagging** is the SIGNiX feature initially showcased in this application. Text Tagging was introduced to the SIGNiX
API in August 2024. It allows signature and other fields to be placed on dynamic documents, anchored by a specific and unique string
on the page. This is ideal for dynamically populated documents, when they document generation system does not directly support
the placement of PDF fields and signature tags.

Over time, this project will be updated to showcase new features.

This application was written to run on WSL and with Visual Studio Code. It should be easily portable to other environments.

## Table of Contents
- Installation
- Usage
- Contributing
- License
- Contact

## Installation
Steps to install the project.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
2. Navigate to the project directory:
   cd yourproject
3. Install the dependencies:
   pip install -r requirements.txt
4. Set up environmental variables

## Usage
How to use the project.

## Contributing
Guidelines for contributing.

## License
The license under which the project is distributed.

## Contact
Your contact information.
