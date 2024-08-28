from flask import Flask, render_template, make_response, redirect, request
import pdfkit
import requests
import os    # used to get environment variables and read files
import re    # used to extract the url from the SIGNiX submit document request
import html  # used to unescape the url returned by SIGNiX
from num2words import num2words # used to get cardinal numberals from integers
from lease_data_initialize import lease_data_create
from docs_data_initialize import docs_data_create
from signer_data_initialize import signer_data_create
from prep_documents import prep_docs
from sx_request_initialize import sx_request_init

app = Flask(__name__)

signer_data = signer_data_create()
docs_data = docs_data_create()
lessee_name = signer_data['signers'][1]['first_name'] + " " + signer_data['signers'][1]['last_name']
lease_data = lease_data_create(lesse_name=lessee_name)

@app.route("/")
def home():
     return render_template("home.html")

@app.route("/lease_template/")
def leasetemplate():
     return render_template("zoom-lease-agreement - Static.html")

@app.route("/lease_data/")
def leasedata():
     return render_template("lease-data.html", lease_data=lease_data)

@app.route("/lease_merged/")
def leasemerged():
     return render_template("zoom-lease-agreement.html", data=lease_data)

@app.route("/preview/")
def preview():
    docs_list = prep_docs(lease_data=lease_data, docs_data=docs_data)

    response = make_response(docs_list[0])
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response

@app.route("/signer_data/")
def signerdata():
     return render_template("signer-form.html", data=signer_data)

@app.route("/submit_tx/")
def submit_tx():
    docs_list = prep_docs(lease_data=lease_data, docs_data=docs_data)

    transaction_data = sx_request_init(docs_list=docs_list, docs_data=docs_data, signer_data=signer_data)
    url = os.getenv('signix_service_url')
    response = requests.post(url, data=transaction_data)

    # print(response.text)

    signer_escaped_url = re.search('<PickupLink>(.*?)</PickupLink>', response.text).group(1)
    signer_url = html.unescape(signer_escaped_url)

    return redirect(signer_url)

@app.route('/update_signer_data', methods=['POST'])
def update_signer_data():
    # Update submitter data
    signer_data['submitter']['name'] = request.form['submitter_name']
    signer_data['submitter']['email'] = request.form['submitter_email']

    # Update signers data
    for i, signer in enumerate(signer_data['signers']):
        signer['first_name'] = request.form[f'first_name_{i+1}']
        signer['middle_name'] = request.form[f'middle_name_{i+1}']
        signer['last_name'] = request.form[f'last_name_{i+1}']
        signer['email'] = request.form[f'email_{i+1}']
        signer['service'] = request.form[f'service_{i+1}']

    return 'Signer data updated successfully'

if __name__ == "__main__":
        app.run(debug=True)