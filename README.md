# Zoom Jet Packs, Powered by SIGNiX
![Zoom-Jet-Packs-Logo-transparent-background-400x400](https://github.com/user-attachments/assets/db329363-cef2-4908-9482-96ee80712bd6)
![SIGNiX (4c) (Custom)](https://github.com/user-attachments/assets/af5bbf18-ee52-41b3-9637-cd28c5537ac4)

## Description
[SIGNiX](https://www.signix.com/) digital signature platform is integrated into a simple Python Flask web application.

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
object structures), so a database is not necessary. For clarity, the code is not hardened. For example, inputs are not validated / cleaned, as 
would be the case with a Production system.

**Text Tagging** is the SIGNiX feature initially showcased in this application. Text Tagging was introduced to the SIGNiX
API in August 2024. It allows signature and other fields to be placed on dynamic documents, anchored by a specific and unique string
on the page. This is ideal for dynamically populated documents, when they document generation system does not directly support
the placement of PDF fields and signature tags.

Over time, this project will be updated to showcase new features.

This application was written to run on WSL and with Visual Studio Code. It should be easily portable to other environments.

## Table of Contents
- Installation
- Usage
- Code Structure and Explanation
- Contributing
- License
- Contact

## Installation
Steps to install the project.

1. Clone the repository:
   ```bash
   git clone https://github.com/kmsignix/zoom-jet-packs
2. Navigate to the project directory:
   ```bash
   cd zoom-jet-packs
3. Create a Python virtual environment and activate it. For example:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
4. Download and install wkhtmltopdf, and then check it by displaying the version. On WSL, for example:
   ```bash
   wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
   sudo apt install -f ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
   wkhtmltopdf --version
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
6. Set up environmental variables. This project uses environment variables to contain credentials and signer-specific data (so they don't appear in code). In VSC, these can be put in the `launch.json` file. For example:
   ```json
   "env": {
                "FLASK_APP": "app.py",
                "FLASK_DEBUG": "1",
                "signix_service_url": "{{SERVICE_URL}}",
                "sponsor": "{{YOUR_SPONSOR_NAME}}", 
                "client": "{{YOUR_CLIENT_NAME}}", 
                "user_id": "{{USERNAME}}", 
                "pswd": "{{PASSWORD}}", 
                "workgroup": "SDD", 
                "demo": "yes",
                "del_docs_after": "60", 
                "email_content": "Your documents for the Sample Application are available online for viewing and signing.",
                "submitter_first_name": "{{YOUR_FIRST_NAME}}",
                "submitter_last_name": "{{YOUR_LAST_NAME}}",
                "submitter_email": "{{YOUR_EMAIL}}",
                "signer1_email": "{{YOUR_OTHER_EMAIL}}",
                "signer1_mobile_number": "{{YOUR_MOBILE_NUMBER}}"
            },

## Usage
Running the application can be done in the VSC debug module, or otherwise. Port 5000 will be opened (typically on localhost), and will serve pages to a web browser. There is a home page and a menu bar.
<<<001-app-home>>>

The application has a template for dynamically creating a lease document. Click `Lease Template` to view a static version of that template, in HTML format.
<<<002-app-template-static>>>

When the application first initializes, it creates data for a lease transaction. Click `Lease Data` to view that data. The jet_pack_list is like a cart, with one item.
<<<003-app-lease-data>>>

The app dynamically generates the lease document by populating the template with the data. Click `Data Merged` to see the result in HTML.
<<<004-app-template-merged>>>

A PDF version of the dynamically generated lease document is generated using pdfkit. Click `PDF` to view it.
<<<005-app-pdf-generated>>>

Signer data is needed to determine the signers of the transaction. This app has two signers. The first signer is the lease manager, who is also the submitter of the transaction. They sign only the lease document. The second signer is the lessee. They sign the lease document, and also a safety advisory document, to acknowledge they have read and understood instructions on safe operation. This second document is the same (static) for all signers, and therefore is a static PDF containing a PDF signature field and a field for the date. To view or edit some of the signer data, click on `Signer Data`.
<<<006-app-signer-data>>>

To submit the transaction for signing, click on `SIGN`. Because the lease manager is the first to sign the lease document, the app automatically redirects to SIGNiX to begin the signing experience for the lease maanger. Click **Accept** to agree to legal consent and terms of service, then click **Next**.
<<<007-SIGNiX-Welcome>>>

Enter your SIGNiX password and click **Next**:
<<<008-SIGNiX-Password>>>

Click **Let Me Review** to view the document:
<<<009-SIGNiX-Review>>>

Click **Sign** to sign the document:
<<<010-SIGNiX-Sign>>>

Click **Finish** to finish signing as the lease manager.
<<<011-SIGNiX-Finish-Signing>>>

The lease manager is then notified that the transaction has been sent to the lessee. Click **Logout**.
<<<012-SIGNiX-Signing-Complete>>>

Switch to your other email, to see there's an invite for the lessee.
<<<013-SIGNiX-gmail-inbox>>>

Open the email, to see the link to the signing experience. Click the link.
<<<014-SIGNiX-email>>>

Click **Accept** to agree to legal consent and terms of service, enter the one-time passcode sent to your mobile device, and then click **Next**.
<<<015-SIGNiX-otp>>>

Enter your SIGNiX password for your other account, to complete your login, and click **Next**. On the next screen, click **Go!**.
<<<016-SIGNiX-password>>>

Click **Sign** to sign the document. Note that lease manager's signature is already on the document, along with the date of their signing.
<<<017-SIGNiX-review>>>

Review the second safety advisory document. Click **Sign**.
<<<018-SIGNiX-sign-2>>>

Enter your password to legally bind your signature to the documents, and click **Sign**.
<<<019-SIGNiX-bind>>>

View the end-of-signing call-to-action. This is to encourage the lessee to now visit the accessories store, and presents a valuable coupon. Click on the link to visit the store, click **Review** to review the document, or click **Logout**.
<<<020-SIGNiX-call-to-action>>>

At the end of the signing, both the lessor and the lesse are sent emails for them to download the documents.

## Code Structure and Explanation


## Contributing
Guidelines for contributing.

## License
The license under which the project is distributed.

## Contact
Your contact information.
