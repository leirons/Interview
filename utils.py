import json
import time
import datetime
import requests
from fake_useragent import UserAgent
import pandas as pd


def get_json_from_history_data(name_of_company: str):
    ua = UserAgent()
    headers = {'user-agent': ua['google chrome']}
    period2 = int(time.mktime(datetime.datetime.now().timetuple()))

    csv_download = f'https://query1.finance.yahoo.com/v7/finance/download/{name_of_company}?period1=1&period2={period2}&interval=1d&events=history&includeAdjustedClose=true'

    # Better way on my opinion
    # df = pd.read_csv(csv_download)
    # return df.to_json(orient='records', lines=True)

    # Way with requests
    r = requests.get(csv_download, headers=headers)
    raw_data = r.text.split(',')
    data = []
    for i in range(6, len(raw_data) - 6, 6):
        data.append({
            raw_data[0]: raw_data[i],
            raw_data[1]: raw_data[i + 1],
            raw_data[2]: raw_data[i + 2],
            raw_data[3]: raw_data[i + 3],
            raw_data[4]: raw_data[i + 4],
            raw_data[5]: raw_data[i + 5],
            raw_data[6].split()[0]: raw_data[6].split()[1]
        })
    return data
