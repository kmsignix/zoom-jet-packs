# This function returns a list of PDFs, generating dynamic documents as necessary

import os
import pdfkit
from flask import render_template

def prep_docs(lease_data, docs_data):
    docs_contents_list = []
    
    for doc in docs_data['docs_list']:
        source_name = doc['doc_source_location']
        source_type = doc['doc_source_type']

        if source_type == "dynamic":
            html_string = render_template(source_name, data=lease_data)
            file_string = pdfkit.from_string(html_string, False)
        elif source_type == "static":
            with open(f"static/{source_name}", 'rb') as file:
                file_string = file.read()
        else:
            print(f"File {source_name} not found.")
            continue
    
        docs_contents_list.append(file_string)

    return docs_contents_list