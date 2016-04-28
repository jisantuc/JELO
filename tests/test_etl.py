import json
from collections import Counter
import pytest

from ..etl.utils import (
    to_json_list, to_jel_letters
)
from ..etl.featurization import (
    json_to_bow
)

inflines = open('tests/test_data.json', 'r').readlines()
dummy_json_list = {
    'Url': 'http://...',
    'Abstract': 'The quick quick brown brown dog.',
    'JelCodes': ['C23', 'C43', 'D15'],
    'Citation': 'Important People. Important Journa. Important Pub Date'
}

def test_to_json_list(lines=inflines):
    assert (
        to_json_list(lines) ==
        map(json.loads, map(lambda x: x.strip(), lines))
    )

def test_to_jel_letters():
    codes = ['C01', 'D39', 'Z29']
    assert to_jel_letters(codes) == {'C', 'D', 'Z'}
    codes = ['C01', 'C03', 'D93']
    assert to_jel_letters(codes) == {'C', 'D'}
    codes = ['09', 'D32']
    with pytest.raises(ValueError):
        to_jel_letters(codes)
    codes = ['0D9', 'A23']
    with pytest.raises(ValueError):
        to_jel_letters(codes)

def test_json_to_bow(js=dummy_json_list):
    assert (
        json_to_bow(js) ==
        {'Url': js['Url'],
         'Abstract': js['Abstract'],
         'JelCodes': js['JelCodes'],
         'Citation': js['Citation'],
         'BoW': dict(Counter(['quick', 'quick', 'brown', 'brown']))}
    )
