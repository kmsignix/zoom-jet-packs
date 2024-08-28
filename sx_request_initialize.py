# This function initializes the SIGNiX SubmitDocuments request

import os
from sx_request_create_functions import *

def sx_request_init(docs_list, docs_data, signer_data):

    tranaction_id=sx_transaction_id_create(prepend_string="ZoomJPakLease")
   
    forms_list = []
    for i, doc in enumerate(docs_data['docs_list']):
        tag_list = []
        tagging_type = doc['tagging_type']
        
        if tagging_type == "text_tagging":
            # make the list of tag elements            
            for tag in doc['tagging_data']:
                if tag['field_type'] == "date_signed":
                    tag_element = sx_element_text_tag_field_create(
                        anchor_text=tag['anchor_text'],
                        x_offset=tag['bounding_box']['x_offset'],
                        y_offset=tag['bounding_box']['y_offset'],
                        width=tag['bounding_box']['width'],
                        height=tag['bounding_box']['height'],
                        is_required=tag['is_required'],
                        tag_name=tag['tag_name']
                        )
                elif tag['field_type'] == "signature":
                    tag_element = sx_element_text_tag_signature_create(
                        anchor_text=tag['anchor_text'], 
                        x_offset=tag['bounding_box']['x_offset'],
                        y_offset=tag['bounding_box']['y_offset'],
                        width=tag['bounding_box']['width'],
                        height=tag['bounding_box']['height'],
                        is_required=tag['is_required'],
                        member_info_number=tag['member_info_number'],
                        date_signed_tag_name=tag['date_signed_field_name'],
                        date_signed_format=tag['date_signed_format']
                        )
                else:
                    print(f"Text tagging field type {tagging_type} / {tag['field_type']} not expected.")

                tag_list.append(tag_element)

        elif tagging_type == "pdf_fields":
            # make the list of tag elements            
            for tag in doc["tagging_data"]:
                if tag['field_type'] == "signature":
                    tag_element = sx_element_signature_line_create(
                        member_info_number=tag["member_info_number"],
                        sign_field=tag["tag_name"],
                        date_signed_field=tag["date_signed_field_name"],
                        date_signed_format=tag["date_signed_format"]
                        )
                else:
                    print(f"Text tagging field type {tagging_type} / {tag['field_type']} not expected.")
                
                tag_list.append(tag_element)
        else:
            print(f"Tagging type {tagging_type} not expected.")
            continue

        form_item = sx_element_form_create(
            ref_id=doc['ref_id'], 
            desc=doc['desc'], 
            file_name=doc['file_name'], 
            mime_type=doc['mime_type'],
            tag_list=tag_list,
            length=len(docs_list[i]),
            form_file_b64=sx_element_form_data_create_from_pdf_string(docs_list[i])
            )

        forms_list.append(form_item)

    member_info_list = []
    for i, signer in enumerate(signer_data['signers']):
        member_info_element = sx_element_member_info_create(
            ref_id=f"Signer {i}",
            ssn=signer['ssn'], 
            dob=signer['dob'],
            first_name=signer['first_name'],
            middle_name=signer['middle_name'],
            last_name=signer['last_name'],
            email=signer['email'],
            mobile_number=signer['mobile_number'],
            service=signer['service']
        )
        member_info_list.append(member_info_element)

    data = sx_element_data_create(
        transaction_id=tranaction_id, 
        doc_set_description=docs_data['doc_set_description'], 
        file_name="Zoom_Jet_Pack_Lease_02242005_032557.zip", 
        submitter_email=signer_data["submitter"]["email"], 
        submitter_name=signer_data["submitter"]["name"], 
        contact_info=f"If you have a question, please contact {signer_data['submitter']['name']} at {signer_data['submitter']['phone']}.", 
        delivery_type="SDDDC", 
        suspend_on_start="no",
        member_info_list=member_info_list,
        forms_list=forms_list
    )

    cust_info = sx_element_cust_info_create(
        sponsor=os.getenv('sponsor'), 
        client=os.getenv('client'), 
        user_id=os.getenv('user_id'), 
        pswd=os.getenv('pswd'), 
        workgroup=os.getenv('workgroup'), 
        demo=os.getenv('demo'), 
        del_docs_after=os.getenv('del_docs_after'), 
        email_content=os.getenv('email_content')
    )

    transaction = sx_element_transaction_create(
        cust_info=cust_info,
        data=data
    )

    xml_str = ET.tostring(transaction, encoding='utf8', method='xml').decode()

    transaction_data = {
        'method': 'SubmitDocument',
        'request': xml_str
    }

    return transaction_data