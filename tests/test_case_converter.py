import pytest
import coding_roadmap.manipulate_strings as cr

def test_convert_to_camel():
    assert cr.camel_converter("Hello, World.") == "helloWorld"


def test_convert_to_snake():
    assert cr.snake_converter("Hello, World.") == "hello_world"


def test_convert_to_kebab():
    assert cr.kebab_converter("Hello, World.") == "hello-world"


def test_convert_to_pascal():
    assert cr.pascal_converter("Hello, World.") == "HelloWorld"


def test_convert_to_uppercasesnake():
    assert cr.uppercasesnake_converter("Hello, World.") == "HELLO_WORLD"

def test_clean_up():
    assert cr.clean_up("remove spaces and others,;/:") == "removespacesandothers"

def test_polindrom():
    assert True == cr.is_palindrome("A man, a plan, a canal: Panama")

def test_polindrom_with_underscore():
    assert True == cr.is_palindrome("Ab_a")