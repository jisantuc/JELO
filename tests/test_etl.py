import pytest

from ..etl.utils import (
    to_json_list, to_jel_letters
)

inflines = open('test_data.json', 'r').readlines()

def test_to_json_list(lines=inflines):
    assert (
        to_json_list(lines) ==
        map(json.loads, map(lambda x: x.strip(), lines))
    )

def test_to_jel_letters(lines=inflines):
    codes = ['C01', 'D39', 'Z29']
    assert to_jel_letters(codes) == {'C', 'D', 'Z'}
    codes = ['C01', 'C03', 'D93']
    assert to_jel_letters(codes) == {'C', 'D'}
    codes = ['09', 'D32']
    with pytest.raises(ValueError):
        to_jel_letters(codes)

#TODO add tests for featurization from gensim
