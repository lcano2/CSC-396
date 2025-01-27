from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "username": "testuser", "email": "test@example.com"},
]
habits = [
    {"id": 1, "user_id": 1, "title": "Daily Exercise", "description": "Do 30 mins of exercise", "goal": 30, "progress": 5},
]
checkins = [
    {"id": 1, "habit_id": 1, "date": "2025-01-25", "status": "completed"},
]


# Users Endpoints
@app.post("/users")
async def create_user(username: str, email: str, password: str):
    user_id = len(users) + 1
    new_user = {"id": user_id, "username": username, "email": email}
    users.append(new_user)
    return new_user


@app.post("/users/login")
async def login_user(email: str, password: str):
    for user in users:
        if user["email"] == email:
            return {"token": "dummy_token", "user_id": user["id"]}
    return {"error": "Invalid credentials"}


# Habits Endpoints
@app.post("/habits")
async def create_habit(user_id: int, title: str, description: str, goal: int):
    habit_id = len(habits) + 1
    new_habit = {"id": habit_id, "user_id": user_id, "title": title, "description": description, "goal": goal, "progress": 0}
    habits.append(new_habit)
    return new_habit


@app.get("/habits")
async def get_habits(user_id: int):
    return [habit for habit in habits if habit["user_id"] == user_id]


# Check-ins Endpoints
@app.post("/checkins")
async def log_checkin(habit_id: int, date: str):
    checkin_id = len(checkins) + 1
    new_checkin = {"id": checkin_id, "habit_id": habit_id, "date": date, "status": "completed"}
    checkins.append(new_checkin)
    return new_checkin


@app.get("/checkins")
async def get_checkins(habit_id: int):
    return [checkin for checkin in checkins if checkin["habit_id"] == habit_id]
