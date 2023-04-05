# polybar-notion

![polybar-notion](https://user-images.githubusercontent.com/38134965/230176803-1378caa4-b06d-4d70-aa1b-fafc54b03c0e.png)

I've tried various methods to track my to-dos, but they were either too complex or inconvenient. By using this module with Notion, I can easily view my to-dos in the status bar. The way I have it set up, the module displays overdue tasks, tasks for today, and tasks without a due date. When a task's due date arrives, it moves into the today's tasks section, and incomplete tasks move into the overdue section. It's also convenient because I can manage my tasks on either my PC or mobile app, and the updates will be reflected in the status bar.

## Installation

1. Create a to-do list on Notion by going to "Templates" and selecting "To-do list". [Reference Image](https://user-images.githubusercontent.com/38134965/230175312-c043727e-b9c1-46d0-af93-2d8fdaf6343c.png)

2. Obtain an API key from Notion by following the instructions at https://developers.notion.com/docs/create-a-notion-integration.

3. Obtain the database ID by copying the link to your to-do list in Notion. The database ID is the string of characters between "https://www.notion.so/" and "?v=" in the link.

4. In your Notion integration settings, go to "Add Connections" and select the integration you created in step 2. [Reference Image](https://user-images.githubusercontent.com/38134965/230175322-4e1f56bd-fa40-4770-acdb-1a69b3e141f8.png)

5. Create a config.json file in the same directory as main.py with the following contents, replacing the values with your own API key and database ID:

```
{
  "NOTION_API_KEY": "secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "NOTION_DATABASE_ID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

6. Edit main.py and change the path to your own config.json.

## Module

```
[module/notion]
type = custom/script
interval = 10.0

exec = python -u ~/.config/polybar/custom-modules/notion/main.py
tail = true

click-left = xdg-open https://notion.so/
```
