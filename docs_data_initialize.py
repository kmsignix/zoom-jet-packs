# This function is used to create an object that is used to populate the docs data

def docs_data_create():
    docs_data = {
        "doc_set_description": "Zoom Jet Pack Lease Documents",
        "docs_list": [
            {
                "ref_id": "ZoomJetPackLease",
                "desc": "Zoom Jet Pack Lease",
                "file_name": "ZoomJetPackLease.pdf",
                "mime_type": "application/pdf",
                "doc_source_type": "dynamic",
                "doc_source_location": "zoom-lease-agreement.html",
                "tagging_type": "text_tagging",
                "tagging_data": [
                    {
                        "tag_name": "LesseeDate",
                        "field_type": "date_signed",
                        "is_required": "yes",
                        "anchor_text": "Date:",
                        "bounding_box": {
                            "x_offset": 30,
                            "y_offset": 0,
                            "width": 90,
                            "height": 12
                        }
                    },
                    {
                        "tag_name": "LessorDate",
                        "field_type": "date_signed",
                        "is_required": "yes",
                        "anchor_text": "As Of:",
                        "bounding_box": {
                            "x_offset": 30,
                            "y_offset": 0,
                            "width": 90,
                            "height": 12
                        }
                    },
                    {
                        "tag_name": "Lessor",
                        "field_type": "signature",
                        "is_required": "yes",
                        "anchor_text": "LESSOR:",
                        "bounding_box": {
                            "x_offset": 150,
                            "y_offset": 6,
                            "width": 120,
                            "height": 24
                        },
                        "member_info_number": 1,
                        "date_signed_field_name": "LessorDate",
                        "date_signed_format": "MM/dd/yy"
                    },
                    {
                        "tag_name": "Lessee",
                        "field_type": "signature",
                        "is_required": "yes",
                        "anchor_text": "LESSEE:",
                        "bounding_box": {
                            "x_offset": 45,
                            "y_offset": 6,
                            "width": 120,
                            "height": 24
                        },
                        "member_info_number": 2,
                        "date_signed_field_name": "LesseeDate",
                        "date_signed_format": "MM/dd/yy"
                    }
                ]
            },
            {
                "ref_id": "ZoomJetPackSafetyAdvisory",
                "desc": "Zoom Jet Pack Safety Advisory",
                "file_name": "ZoomJetPackSafetyAdvisory.pdf",
                "mime_type": "application/pdf",
                "doc_source_type": "static",
                "doc_source_location": "zoom-safety-advisory.pdf",
                "tagging_type": "pdf_fields",
                "tagging_data": [
                    {
                        "tag_name": "SignatureField",
                        "field_type": "signature",
                        "member_info_number": 2,
                        "date_signed_field_name": "DateField",
                        "date_signed_format": "MM/dd/yy"
                    }
                ]
            }
        ]
    }

    return docs_data