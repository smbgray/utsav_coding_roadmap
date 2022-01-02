import re

def convert(input: str, case: str) -> str:
    
    return ""

def clean_up (input: str) -> str:
    
    cleaned_string = re.sub(r'\W+','', input)
    return cleaned_string

def camel_converter(input: str) -> str:
    res = input.split()
    result = [word.capitalize() for word in res ]
    result[0] = result[0].lower()
    return clean_up(''.join(str(word) for word in result ))