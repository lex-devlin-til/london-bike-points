import json
import datetime
import requests
import time

# define url and API response variables
url = f"https://api.tfl.gov.uk/BikePointr"
response = requests.get(url)

current_try = 0
wait_time = 2 # seconds
while current_try < 5:

    try:
        # Raises error if status isn't 200
        response.raise_for_status()

        # Parses the json
        data = response.json()

        # In the case that the json is empty or really short, raises error
        if len(data) < 50:
            raise Exception('json is wayyyy too short!')
        
        # If the time between now and the lastest modified date in the data is more than 2 days, error
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
        
        # Exports data as json 
        filename = datetime.now.strftime('%Y-%m-%d_%H-%M-%S')
        filepath = f'data/{filename}.json'
        print(filename)
        with open(filepath, 'w') as file:
            json.dump(data, file)
        break # stops while loop if everything was successful
    
    # if something went wrong with the request itself, print that error
    except requests.exceptions.RequestException as e:
        print(e)
    # Prints any custom exception, i.e. "json is too short" or "data is stale"
    except Exception as e:
        print(e)
    # Prints whoops if raise_for_status wasn't 200
    except:
        print("Whoops!")

    # adds 1 to current_try, waits to try again
    current_try += 1
    print('waiting, will try again in {wait_time} seconds...')
    time.sleep(wait_time)

# prints a message if we tried too many times
if current_try == 5:
    print('Too many tries. :(')