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
pdfkit. A static PDF containing PDF signature fields is also included.

When the user selects "Sign" from the menu, the application creates a transaction containing the
documents and sends it to SIGNiX via the FLEX API. SIGNiX responds with a link / redirection for the lease 
manager to sign the lease document. Once they have signed, SIGNiX invites the lessee to sign via email,
and uses SMS authentication to ensure the signer is as intended.

This application was written to run on WSL and with Visual Studio Code, although it should be easily portable to other environments.

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
