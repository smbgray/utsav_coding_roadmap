import pytest
import coding_roadmap.manipulate_strings as cr

def test_convert_to_camel():
    assert cr.convert("Hello, World.","camel") == "helloWorld"