"""String manipulations module"""
import re

def convert(provided_string: str, case: str) -> str:
    """Main flow function"""
    if case == "camel":
        return camel_converter(provided_string)

def clean_up (provided_string: str) -> str:
    """Cleans up string from nonalphanumerical characters"""
    cleaned_string = re.sub(r'\W+','', provided_string)
    return cleaned_string

def camel_converter(provided_string: str) -> str:
    """Convert into camel case"""
    result = [word.capitalize() for word in provided_string.split() ]
    result[0] = result[0].lower()
    return clean_up(''.join(str(word) for word in result ))

def snake_converter(provided_string: str) -> str:
    """Convert into snake case"""
    result = [word.lower() for word in provided_string.split() ]
    return clean_up('_'.join(str(word) for word in result ))

def kebab_converter(provided_string: str) -> str:
    """Convert into kebab case"""
    result = [clean_up(word.lower()) for word in provided_string.split() ]
    return '-'.join(str(word) for word in result )

def pascal_converter(provided_string: str) -> str:
    """Convert into pascal case"""
    result = [word.lower() for word in provided_string.split() ]
    return clean_up('-'.join(str(word).capitalize() for word in result ))


def uppercasesnake_converter(provided_string: str) -> str:
    """Convert into kebab case"""
    result = [word.lower() for word in provided_string.split() ]
    return clean_up('_'.join(str(word).upper() for word in result ))

def is_palindrome(provided_string: str) -> bool:
    """vaslidate if string is palindrome"""
    reversed_string = clean_up(provided_string).lower().replace("_","")[::-1]
    if reversed_string == clean_up(provided_string).lower().replace("_",""):
        return True
    else:
        return False
