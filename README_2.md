API Documentation: Habit Tracker
Base URL
http://127.0.0.1:8000
1. Users
Create User
URL: /users
Method: POST
Description: Create a new user account.
Request Body:
json
CopyEdit
{
  "username": "string",
  "email": "string",
  "password": "string"
}

Response:
json
CopyEdit
{
  "id": "integer",
  "username": "string",
  "email": "string",
  "created_at": "string (ISO format)"
}

HTTP Status Codes:
201 Created: User successfully created.
400 Bad Request: Missing or invalid data.

User Login
URL: /users/login
Method: POST
Description: Authenticate a user and return a token.
Request Body:
json
CopyEdit
{
  "email": "string",
  "password": "string"
}

Response:
json
CopyEdit
{
  "token": "string",
  "user_id": "integer"
}

HTTP Status Codes:
200 OK: Login successful.
401 Unauthorized: Invalid credentials.

2. Habits
Create a Habit
URL: /habits
Method: POST
Description: Create a new habit for the user.
Request Body:
json
CopyEdit
{
  "user_id": "integer",
  "title": "string",
  "description": "string",
  "goal": "integer", // Target number of check-ins
  "start_date": "string (ISO format)"
}

Response:
json
CopyEdit
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "goal": "integer",
  "start_date": "string (ISO format)",
  "progress": 0
}

HTTP Status Codes:
201 Created: Habit successfully created.
400 Bad Request: Missing or invalid data.

Get All Habits
URL: /habits?user_id={user_id}
Method: GET
Description: Fetch all habits for a specific user.
Response:
json
CopyEdit
[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "goal": "integer",
    "progress": "integer"
  },
  ...
]

HTTP Status Codes:
200 OK: Successfully retrieved habits.
404 Not Found: No habits found for the user.

3. Check-ins
Log a Check-in
URL: /checkins
Method: POST
Description: Log a daily check-in for a habit.
Request Body:
json
CopyEdit
{
  "habit_id": "integer",
  "date": "string (ISO format)"
}

Response:
json
CopyEdit
{
  "id": "integer",
  "habit_id": "integer",
  "date": "string (ISO format)",
  "status": "string" // e.g., "completed"
}

HTTP Status Codes:
201 Created: Check-in successfully logged.
400 Bad Request: Missing or invalid data.

Get Check-ins for a Habit
URL: /checkins?habit_id={habit_id}
Method: GET
Description: Retrieve all check-ins for a specific habit.
Response:
json
CopyEdit
[
  {
    "id": "integer",
    "date": "string (ISO format)",
    "status": "string"
  },
  ...
]

HTTP Status Codes:
200 OK: Successfully retrieved check-ins.
404 Not Found: No check-ins found for the habit.
