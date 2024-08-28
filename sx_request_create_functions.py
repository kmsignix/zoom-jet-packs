# These functions are used to construct the SIGNiX SubmitDocument request

import base64
import xml.etree.ElementTree as ET
from datetime import datetime

def sx_transaction_id_create(prepend_string):
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
    result = prepend_string + formatted_now
    
    return result

def sx_element_form_data_create_from_pdf_string(pdf_string):
    form_data = ET.Element("Data")
    form_data.text = base64.b64encode(pdf_string).decode()

    return form_data

def sx_element_cust_info_create(sponsor, client, user_id, pswd, workgroup, demo, del_docs_after, email_content):
    cust_info = ET.Element("CustInfo")

    ET.SubElement(cust_info, "Sponsor").text = sponsor
    ET.SubElement(cust_info, "Client").text = client
    ET.SubElement(cust_info, "UserId").text = user_id
    ET.SubElement(cust_info, "Pswd").text = pswd
    ET.SubElement(cust_info, "Workgroup").text = workgroup
    ET.SubElement(cust_info, "Demo").text = demo
    ET.SubElement(cust_info, "DelDocsAfter").text = str(del_docs_after)
    ET.SubElement(cust_info, "EmailContent").text = email_content

    return cust_info

def sx_element_member_info_create(ref_id, ssn, dob, first_name, middle_name, last_name, email, mobile_number, service):
    member_info = ET.Element("MemberInfo")

    ET.SubElement(member_info, "RefID").text = ref_id
    ET.SubElement(member_info, "SSN").text = ssn
    ET.SubElement(member_info, "DOB").text = dob
    ET.SubElement(member_info, "FirstName").text = first_name
    ET.SubElement(member_info, "MiddleName").text = middle_name
    ET.SubElement(member_info, "LastName").text = last_name
    ET.SubElement(member_info, "Email").text = email
    ET.SubElement(member_info, "Service").text = service
    ET.SubElement(member_info, "MobileNumber").text = mobile_number

    return member_info

def sx_element_signature_line_create(member_info_number, sign_field, date_signed_field, date_signed_format):
    signature_line = ET.Element("SignatureLine")

    ET.SubElement(signature_line, "MemberInfoNumber").text = str(member_info_number)
    ET.SubElement(signature_line, "SignField").text = sign_field
    ET.SubElement(signature_line, "DateSignedField").text = date_signed_field
    ET.SubElement(signature_line, "DateSignedFormat").text = date_signed_format

    return signature_line

def sx_element_text_tag_field_create(anchor_text, x_offset, y_offset, width, height, is_required, 
                                     tag_name):
    text_tag_signature = ET.Element("TextTagField")

    ET.SubElement(text_tag_signature, "Type").text = "DateSigned"
    ET.SubElement(text_tag_signature, "AnchorText").text = anchor_text
    ET.SubElement(text_tag_signature, "AnchorXOffset").text = str(x_offset)
    ET.SubElement(text_tag_signature, "AnchorYOffset").text = str(y_offset)
    ET.SubElement(text_tag_signature, "Width").text = str(width)
    ET.SubElement(text_tag_signature, "Height").text = str(height)
    ET.SubElement(text_tag_signature, "IsRequired").text = is_required
    ET.SubElement(text_tag_signature, "TagName").text = tag_name

    return text_tag_signature

def sx_element_text_tag_signature_create(anchor_text, x_offset, y_offset, width, height, is_required, 
                                         member_info_number, date_signed_tag_name, date_signed_format):
    text_tag_signature = ET.Element("TextTagSignature")

    ET.SubElement(text_tag_signature, "MemberInfoNumber").text = str(member_info_number)
    ET.SubElement(text_tag_signature, "AnchorText").text = anchor_text
    ET.SubElement(text_tag_signature, "AnchorXOffset").text = str(x_offset)
    ET.SubElement(text_tag_signature, "AnchorYOffset").text = str(y_offset)
    ET.SubElement(text_tag_signature, "Width").text = str(width)
    ET.SubElement(text_tag_signature, "Height").text = str(height)
    ET.SubElement(text_tag_signature, "IsRequired").text = str(is_required)
    ET.SubElement(text_tag_signature, "DateSignedTagName").text = date_signed_tag_name
    ET.SubElement(text_tag_signature, "DateSignedFormat").text = date_signed_format

    return text_tag_signature

def sx_element_form_create(ref_id, desc, file_name, mime_type, tag_list, length, form_file_b64):
    form = ET.Element("Form")

    ET.SubElement(form, "RefID").text = ref_id
    ET.SubElement(form, "Desc").text = desc
    ET.SubElement(form, "FileName").text = file_name
    ET.SubElement(form, "MimeType").text = mime_type
    for tag in tag_list:
        form.append(tag)
    ET.SubElement(form, "Length").text = str(length)
    form.append(form_file_b64)

    return form

def sx_element_data_create(transaction_id, doc_set_description, file_name, submitter_email, submitter_name, contact_info, delivery_type, suspend_on_start, member_info_list, forms_list):
    # Requires member_info and form elements to be supplied, so they can be appended
    data = ET.Element("Data")

    ET.SubElement(data, "TransactionID").text = transaction_id
    ET.SubElement(data, "DocSetDescription").text = doc_set_description
    ET.SubElement(data, "FileName").text = file_name
    ET.SubElement(data, "SubmitterEmail").text = submitter_email
    ET.SubElement(data, "SubmitterName").text = submitter_name
    ET.SubElement(data, "ContactInfo").text = contact_info
    ET.SubElement(data, "DeliveryType").text = delivery_type
    ET.SubElement(data, "SuspendOnStart").text = suspend_on_start
    for member_info in member_info_list:
        data.append(member_info)
    for form in forms_list:
        data.append(form)
 
    return data

def sx_element_transaction_create(cust_info, data):
    # Requires cust_info and form elements
    transaction = ET.Element("SubmitDocumentRq", xmlns="urn:com:signix:schema:sdddc-1-1")
    transaction.append(cust_info)
    transaction.append(data)

    return transaction