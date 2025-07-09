import json
import datetime
import requests

# define url and API response variables
url = f"https://api.tfl.gov.uk/BikePoint"
response = requests.get(url)

try:
    response.raise_for_status()
    data = response.json()
    
    if len(data) < 50:
        raise Exception('json is wayyyy too short!')
    
    now = datetime.now()
    dates_list = []
    for item in data:
        for attribute in item.get('additionalProperties', []):
            if "modified" in attribute:
                dates_list.append(attribute["modified"])

    max_date = datetime.strptime(max(dates_list), '%Y-%m-%dT%H:%M:%S.%fZ')
    delta = now - max_date
    if delta.days > 2:
        raise Exception('This data is stale... yeesh.')
    
    filename = datetime.now.strftime('%Y-%m-%d_%H-%M-%S')
    filepath = f'data/{filename}.json'
    print(filename)
    with open(filepath, 'w') as file:
        json.dump(data, file)
except requests.exceptions.RequestException as e:
    print(e)
except Exception as e:
    print(e)
except:
    print("Whoops!")








