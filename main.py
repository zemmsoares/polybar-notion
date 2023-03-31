import requests
import json

with open('/home/zemmsoares/.config/polybar/custom-modules/polybar-notion/config.json', 'r') as f:
    config = json.load(f)

NOTION_API_KEY = config['NOTION_API_KEY']
NOTION_DATABASE_ID = config['NOTION_DATABASE_ID']

# Define the API endpoint URL
url = 'https://api.notion.com/v1/databases/' + NOTION_DATABASE_ID + '/query'

# Define the request headers
headers = {
    'Authorization': 'Bearer ' + NOTION_API_KEY,
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}

data = {}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response status code
if response.status_code == 200:

    # Initialize counters
    todo_count = 0
    done_count = 0
    # Loop through the results and print the task titles
    for result in response.json()['results']:
        title = result['properties']['Status']['select']['name']
        status = result['properties']['Name']['title'][0]['text']['content']

        # Increment the counter
        if title == 'To Do':
            todo_count += 1
        elif status == 'Done':
            title += 1
        
    print(f"%{{F#de4c4a}}Todo: %{{F-}}{todo_count} %{{F#f49c18}}Done: %{{F-}}{done_count}")

else:
    print('Error:', response.status_code)
    print(response.text)