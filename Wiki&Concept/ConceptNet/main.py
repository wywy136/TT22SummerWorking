import requests
obj = requests.get('http://api.conceptnet.io/c/en/example').json()

# print(obj['edges'][2])

print([(edge['start']['@id'], edge['end']['@id'], edge['rel']['@id'], edge['surfaceText']) for edge in obj["edges"]])