#!/bin/env python3
"""
Creates currency data fixture from LANG django variable
"""
import babel.numbers
import json


def currency_data():
    """
    Returns list of all currency symbols
    """

    data = []
    i = 1
    for symbol in babel.numbers.list_currencies():
        dat = {}
        dat['model'] = 'providers.currency'
        dat['pk'] = i
        dat['fields'] = {'symbol': symbol}

        data.append(dat)
        i += 1

    return data


if __name__ == '__main__':
    data = currency_data()
    with open('currency_data.json', 'w') as f:
        f.write(json.dumps(data))
