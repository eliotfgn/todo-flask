# Todo Flask
This is a basic CRUD on todo, made with Flask.

# How to use
1. Clone this repository
2. Create a virtualenv with Python 3 using `virtualenv -p python3 venv`
3. Activate your virtualenv using `source venv/bin/activate` or `venv\Scripts\activate` if you are using powershell
4. Install the requirements using `pip install -r requirements.txt`
5. Run the application using `flask run`

# API endpoints
## GET /todos
Get all todos
## GET /todos/:id
Get a todo by id (id is a number)
## POST /todos
Create a todo
### Body
```json
{
  "title": "Title",
  "description": "Todo description.",
  "deadline": "2023-03-17 13:40:30",
  "remind": "2023-03-17 13:13:30"
}
```
## PUT /todos/:id
Update a todo by id (id is a number)
### Body
```json
{
  "title": "New Title",
  "description": "Todo new description.",
  "deadline": "2023-03-17 13:40:30",
  "remind": "2023-03-17 13:13:30"
}
```

## DELETE /todos/:id
Delete a todo by id (id is a number)

# Features
- [x] Create a todo
- [x] Read a todo
- [x] Update a todo
- [x] Delete a todo
- [x] Remind a todo
- [X] Remind a todo 30 min before deadline