import pytest
import coding_roadmap.manipulate_strings as cr

def test_convert_to_camel():
    assert cr.camel_converter("Hello, World.") == "helloWorld"

def test_clean_up ():
    assert cr.clean_up("remove spaces and others,;/:") == "removespacesandothers"