This directory contains two scrips for generating fixtures:
    - language_data.py: creates fixture language_data.json from django locale data
    - currency_data.py: creates fixture currency_data.json from babel currencies
Usage:
    - Run the scripts to generate the fixtures
    - Load the fixtures
        ./manage.py loaddata language_data
        ./manage.py loaddata currency_data
    
