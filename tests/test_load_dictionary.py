from unittest.mock import patch, mock_open
import sys, os


import load_dictionary

# _temp = importlib.import_module(".load_dictionary.py", package="src")
# load = _temp.load
# print(sys.path)
# import importlib


def test_load_dictionary_file():
    fake_file_path = ".src/bob"
    file_content_mock = "mock\nword\nhallelujah"

    with patch("builtins.open", new=mock_open(read_data=file_content_mock)) as _file:
        actual = load_dictionary.load(fake_file_path)
        expected = file_content_mock.split()
        assert expected == actual


def test_load_dictionary_bad():
    fake_file_path = "file/path/mock.txt"
    try:
        # this line
        load_dictionary.load(fake_file_path)
        assert False
    except AssertionError:
        assert True
