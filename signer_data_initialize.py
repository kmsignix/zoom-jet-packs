# This function is used to create an object that is used to populate the signer data
import os    # used to get environment variables and read files

def signer_data_create():

    submitter_first_name = os.getenv('submitter_first_name')
    submitter_middle_name = ""
    submitter_last_name = os.getenv('submitter_last_name')
    submitter_email = os.getenv('submitter_email')
    submitter_phone = "800-555-1234"

    default_ssn = "910000000"
    default_dob = "00/00/0000"
    default_mobile_number = "1112223333"
    default_service = "SelectOneClick"

    signer_data = {
        "submitter": {
            "name": submitter_first_name + " " + submitter_last_name,
            "email": submitter_email,
            "phone": submitter_phone
        },
        "signers": [
             {
                "first_name": submitter_first_name,
                "middle_name": submitter_middle_name,
                "last_name": submitter_last_name,
                "email": submitter_email,
                "ssn": default_ssn,

                "dob": default_dob,
                "mobile_number": default_mobile_number,
                "service": default_service,
                "call_to_action": {
                    "imageURL": "https://www.signix.com/hubfs/Sample%20Marketing%20Link%20Images/sample%20marketing%20graphic.png",
                    "imageURLhover": "https://www.signix.com/hubfs/Sample%20Marketing%20Link%20Images/signix-ad-hover.png",
                    "targetURL": "https://www.signix.com",
                    "imageLocation": "Above Text",
                    "imageHeight": 600,
                    "imageWidth": 600,
                    "imageAltText": "Learn more about SIGNiX"
                }
            },
            {
                "first_name": "Max",
                "middle_name": "Danger",
                "last_name": "Fun",
                "email": os.getenv('signer1_email'),
                "ssn": default_ssn,
                "dob": default_dob,
                "mobile_number": os.getenv('signer1_mobile_number'),
                "service": "SMSOneClick",
                "call_to_action": {
                    "imageURL": "https://www.signix.com/hubfs/Karl.png",
                    "imageURLhover": "https://www.signix.com/hubfs/karl-hover.png",
                    "targetURL": "https://www.figma.com/design/CMr9rSH8McKSACGZyOhPNd/Zoom-Jet-Packs-Store?node-id=0-1&t=dsOv3vlnVL9Sli9c-0",
                    "imageLocation": "Below Text",
                    "imageHeight": 600,
                    "imageWidth": 600,
                    "imageAltText": "Zoom Jet Packs Store"
                }
            }
        ]
    }

    return signer_data