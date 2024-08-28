# This function is used to create an object that is used to populate the lease template

from num2words import num2words

def lease_data_create(lesse_name):
    jet_pack_list = [
        {
            "sku": "Skyward Personal Jetpack P-2024",
            "year": "2024",
            "jpin": "4CH8P4K7E3X6Z9R2V"
        }
    ]
    
    lease_data = {
        "entered_day": "14th",
        "entered_month": "August",
        "entered_year": "2024",
        "lessee_name": lesse_name,
        "number_of_items_text": num2words(len(jet_pack_list)),
        "number_of_items_number": len(jet_pack_list),
        "number_of_items_inflection": "" if len(jet_pack_list) == 1 else "s",
        "jet_pack_list": jet_pack_list,
        "lease_start_day_month": "September 1",
        "lease_start_year": "2024",
        "lease_end_day_month": "August 31",
        "lease_end_year": "2029",
        "payment_amount": "1,199",
        "payment_period": "month",
        "security_deposit": "1,000",
        "insurance_amount": "100,000",
        "governing_law": "Delaware"
    }

    return lease_data