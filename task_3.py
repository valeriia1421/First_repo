import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)
    
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            normalized_number = '+' + cleaned_number
        else:
            normalized_number = '+38' + cleaned_number
    else:
        normalized_number = cleaned_number
    
    return normalized_number

test_numbers = [
    "+380 50 123 4567",
    "0501234567",
    "+1 234 567 8900",
    "(050) 123-45-67",
    "380501234567",
    "+380501234567"
]

normalized_numbers = [normalize_phone(num) for num in test_numbers]
print(normalized_numbers)