#!/bin/env python3
"""
Creates language data fixture from LANG django variable
"""
from django.conf.locale import LANG_INFO
import json
import os

# cwd to the current script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



def language_data():
    """
    Gets language data from LANG_INFO
    Returns: list, language data
    """
    langs = dict(LANG_INFO)

    # proper fallbacks
    for key, val in langs.items():
        if langs[key].get('fallback'):
            fallback_key = langs[key]['fallback'][0]
            langs[key] = langs[fallback_key]

    # insert data
    data = []
    i = 1
    for key in langs:
        fields = {}
        fields['code'] = key
        fields['bidi'] = langs[key]['bidi']
        fields['name'] = langs[key]['name']
        fields['name_local'] = langs[key]['name_local']

        dat = {}
        dat['model'] = 'providers.language'
        dat['pk'] = i
        dat['fields'] = fields

        data.append(dat)
        i += 1

    return data


if __name__ == '__main__':
    data = language_data()
    with open('language_data.json', 'w') as f:
        f.write(json.dumps(data))
