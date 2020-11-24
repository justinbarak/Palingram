from unittest.mock import patch, mock_open
import sys, os

print(sys.path)
import load_dictionary


def test_load_dictionary_file():
    fake_file_path = "..src/"
    file_content_mock = r"mock\nword\nnew\ntest"

    with patch("__main__.open", new=mock_open(read_data=file_content_mock)) as _file:
        actual = load_dictionary.load(fake_file_path)
        expected = file_content_mock
        assert expected == actual


def test_load_dictionary_bad():
    fake_file_path = "file/path/mock.txt"
    try:
        load_dictionary.load(fake_file_path)
        assert False
    except IOError:
        assert True
