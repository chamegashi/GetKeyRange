import requests
import KeyParser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('keywords', type=str, nargs='*')
args = parser.parse_args()

keyword = ""
for word in args.keywords:
    keyword = keyword + word + "+"

res = requests.get("https://keytube.net/search/?word=" + keyword[:-1])
parser = KeyParser.KeyDataParser()
parser.feed(res.text)
data = parser.found_td_data[1:]
print(data)
