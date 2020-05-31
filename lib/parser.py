from functools import reduce
from collections.abc import Sequence, Mapping
import json


def get_with_array_check(dictionary, key):
    '''
    Finds the value of a key in a dictionary.
    Returns the value, or the value of an index from it in case the key has an array-access

    Arguments:
    dictionary: dict where to look for the key
    key: key to search in the dictionary. may contain an index.

    Returns: value of the key if found, None otherwise
    '''
    if '[' in key:
        actual_key, index = key[:-1].split('[')
        value = dictionary.get(actual_key)
        index = int(index)
        if value and isinstance(value, Sequence) and len(value) > index:
            return value[index]
    else:
        return dictionary.get(key)


def get_attributes(dictionary, attributes):
    '''
    Parses a json string and returns only relevant fields in it.

    Arguments:
    dictionary: json valid string with the data to extract
    attributes: list of dot-noted fields to extract from dictionary

    Returns: Dict with the attributes extracted.
    '''
    try:
        json_dict = json.loads(dictionary)
        result = dict()
        for att in attributes:
            att_list = att.split('.')
            value = (reduce(lambda d, key: get_with_array_check(d, key)
                     if d and isinstance(d, Mapping) else None,
                     att_list, json_dict))
            if value:
                result[att] = value
        return result
    except Exception as e:
        print(f'Error getting attributes: {e}')
        print(f'Dict: {dictionary}')
