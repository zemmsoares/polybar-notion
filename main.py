import requests
from datetime import datetime
import json

with open('/home/zemmsoares/.config/polybar/custom-modules/notion/config.json', 'r') as f:
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


   # Initialize the dictionaries and lists
    tasks_by_date = {}
    tasks_no_due_date = []
    tasks_overdue = []

    # Loop through the results
    for result in response.json()['results']:
        try:
            status = result['properties']['Status']['select']['name']
        except KeyError:
            status = None
            
        try:
            title = result['properties']['Name']['title'][0]['text']['content']
        except (KeyError, IndexError):
            title = None
            
        try:
            due_date = result['properties']['Due Date']['date']['start']
        except (KeyError, TypeError):
            due_date = None


        # Add the task to the appropriate group
        if due_date == None and status == 'To Do':
            tasks_no_due_date.append(result)
        elif due_date == datetime.today().strftime('%Y-%m-%d') and status == 'To Do':
            if due_date not in tasks_by_date:
                tasks_by_date[due_date] = [result]
            else:
                tasks_by_date[due_date].append(result)
        elif status == 'To Do' and due_date < datetime.today().strftime('%Y-%m-%d'):
            tasks_overdue.append(result)
    
    # Print the results
    today_count = len(tasks_by_date.get(datetime.today().strftime('%Y-%m-%d'), []))
    #print(f'Tasks Due Today ({datetime.today().strftime("%Y-%m-%d")}): {today_count}')

    no_due_date_count = len(tasks_no_due_date)
    #print('\nTasks with No Due Date:', no_due_date_count)

    overdue_count = len(tasks_overdue)
    #print('\nTasks Overdue:', overdue_count)

    print('%{{BEC407A}} {} %{{B#00B19F}} {} %{{B#444444}} {} '.format(overdue_count, today_count, no_due_date_count))

else:
    print('Error:', response.status_code)
    print(response.text)