import pandas as pd
import numpy as np

import json
from bs4 import BeautifulSoup

if __name__ == '__main__':

    bigfoot_records = []
    with open('data/bigfoot_first100records.json') as f:
        for i in f:
            bigfoot_records.append(json.loads(i))

    soup = BeautifulSoup(bigfoot_records[0]['html'], 'html.parser')

    p_elms = soup.find('table').find_all('p')
    for p in p_elms:
        print(p.text)
