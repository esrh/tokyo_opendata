import json, os, time
import requests as r

def token():
    with open(os.path.expanduser('~\\important\\token.json'), 'r') as hoge:
        token = json.load(hoge)['metro']
    return token


def journeys(token):
    endpoint = 'https://api.tokyometroapp.jp/api/v2/'
    tokenu = 'acl:consumerKey=' + token
    uri = 'datapoints?rdf:type=odpt:Station&odpt:railway=odpt.Railway:TokyoMetro.Marunouchi&acl:consumerKey=' + token
    url = endpoint + uri
    print(url)
    res = json.loads(r.get(url).text)
    a = [hoge['odpt:passengerSurvey'] for hoge in res]
    print(a)
    for x in a:
        for xx in x:
            url = endpoint + "datapoints/{}?{}".format(xx, tokenu)
            print(url)
            journeys = json.loads(r.get(url).text)[0]["odpt:passengerJourneys"]
            print(journeys)
            time.sleep(1)

def train_info(token):
    latlon = (35.690921, 139.700258)
    endpoint = 'https://api.tokyometroapp.jp/api/v2/'
    uri = 'places?rdf:type=odpt:Station&lat={0[0]}&lon={0[1]}&radius=100&acl:consumerKey={1}'.format(latlon, token)


def main():
    token = token()
    journeys(token)
