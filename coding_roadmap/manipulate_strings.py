"""String manipulations module"""
import re

def convert(input: str, case: str) -> str:
    """Main flow function"""
    return ""

def clean_up (input: str) -> str:
    """Clean up string from nonalphanumerical characters"""
    cleaned_string = re.sub(r'\W+','', input)
    return cleaned_string

def camel_converter(input: str) -> str:
    """Convert into camel case"""
    result = [word.capitalize() for word in input.split() ]
    result[0] = result[0].lower()
    return clean_up(''.join(str(word) for word in result ))
