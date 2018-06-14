import json, os, time, csv
import requests as r
import pandas as pd

def set_token():
    with open(os.path.expanduser('~\\important\\token.json'), 'r') as hoge:
        token = json.load(hoge)['metro']
    return token

def route_table(route):
    df = pd.read_csv('route_table.csv')
    for i, row in df.iterrows():
        if row['route'] == route:
            return row['ID']
    raise

def journeys(token, route=None, _id=None):
    rt = []
    if _id is None:
        _id = route_table(route)
    endpoint = 'https://api.tokyometroapp.jp/api/v2/'
    uri = 'datapoints?rdf:type=odpt:Station&odpt:railway={}&acl:consumerKey={}'.format(_id, token)
    url = endpoint + uri
    res = json.loads(r.get(url).text)
    for x in [hoge['odpt:passengerSurvey'] for hoge in res]:
        for xx in x:
            url = endpoint + "datapoints/{}?acl:consumerKey={}".format(xx, token)
            journeys = json.loads(r.get(url).text)[0]["odpt:passengerJourneys"]
            print(xx, journeys)
            rt.append([xx, journeys])
            time.sleep(1)
    return rt
    
def train_info(token):
    latlon = (35.690921, 139.700258)
    endpoint = 'https://api.tokyometroapp.jp/api/v2/'
    uri = 'places?rdf:type=odpt:Station&lat={0[0]}&lon={0[1]}&radius=100&acl:consumerKey={1}'.format(latlon, token)


def main():
    token = set_token()
    data = journeys(token, "丸ノ内線")
    with open('ignore/write.csv', 'w') as f:
        csv.writer(f, lineterminator='\n').writerows(data)
    

main()
