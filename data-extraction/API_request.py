import requests
import json
import pandas as pd

# GETTING A LIST OF AVAILABLE COUNTRIES
countries_api_url = 'https://covid-api.mmediagroup.fr/v1/cases'
countries_data = requests.get(countries_api_url).text
json_data = json.loads(countries_data)

countries = []
for element in json_data:
    countries.append(element)

# GETTING THE HISTORY OF CASES AND DEATHS OF ANY COUNTRY SEPARATELY


def historic_data(countries, status):
    csv = pd.DataFrame()
    for i in countries:
        deaths_url = 'https://covid-api.mmediagroup.fr/v1/history?country={}&status={}'.format(
            i, status)
        deaths_data = requests.get(deaths_url).text
        data = json.loads(deaths_data)
        df = pd.DataFrame.from_dict(data['All']['dates'], orient='index')
        df.index.names = ['date']
        df.insert(0, "country", i, allow_duplicates=False)
        csv = pd.concat([csv, df], ignore_index=False)
        print('{} data: {} DONE'.format(status, i))
    csv.to_csv("{}_data.csv".format(status), header=['country', status])
    print('{} data: 100% DONE'.format(status))


attributes = ('deaths', 'confirmed')

for i in attributes:
    historic_data(countries, i)
