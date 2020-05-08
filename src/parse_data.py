import json
from bs4 import BeautifulSoup 
import re
import pandas as pd

if __name__ == '__main__':

    filename = "../data/bigfoot_first100records.txt"
    records = []
    with open(filename) as f:
        for record in f:
            records.append(json.loads(record))

    # get all headers
    for rec in records:
        soup = BeautifulSoup(rec['html'], 'html.parser')
        p_elms = soup.find('table').find_all('p')
        headers = []
        for p in p_elms:
            if p.find('span')!= None:
                p_head_text = p.find('span').text
                if p_head_text not in headers:
                    headers.append(p_head_text)

    # build table
    df = pd.DataFrame(columns=headers)
    for rec in records:
        soup = BeautifulSoup(rec['html'], 'html.parser')
        p_elms = soup.find('table').find_all('p')
        data_dict = {}
        for p in p_elms:
            if p.find('span')!= None:
                p_head_text = p.find('span').text
                data_dict[p_head_text] = re.sub(fr"^{p_head_text}", "", p.text)
        df = df.append([data_dict])

    # clean column names
    df.columns = [col.lower().replace(":","").replace(" ","_") for col in df.columns]
    
    # pickle and save it
    df.to_pickle('data/{}_pickled_df'.format(filename))