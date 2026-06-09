# Smart Study Planner Agent
# Observe -> Think -> Act

tasks = []

days_order = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

difficulty_days = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

n = int(input("How many tasks do you have? "))

for i in range(n):
    print(f"\nTask {i+1}")

    name = input("Task Name: ")

    deadline = input("Deadline (Monday-Sunday): ").strip().lower()

    hours = int(input("Study Hours Needed: "))

    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().lower()

    tasks.append({
        "name": name,
        "deadline": deadline,
        "hours": hours,
        "difficulty": difficulty
    })

print("\n===== AI STUDY PLAN =====")

for task in tasks:

    deadline_number = days_order[task["deadline"]]

    days_before = difficulty_days[task["difficulty"]]

    study_day_number = deadline_number - days_before

    if study_day_number < 1:
        study_day_number = 1

    study_day = ""

    for day, number in days_order.items():
        if number == study_day_number:
            study_day = day.capitalize()

    print("\n-------------------------")
    print("Task:", task["name"])
    print("Deadline:", task["deadline"].capitalize())
    print("Difficulty:", task["difficulty"].capitalize())
    print("Study Hours:", task["hours"])

    if task["difficulty"] == "hard":
        print("Priority: HIGH")
    elif task["difficulty"] == "medium":
        print("Priority: MEDIUM")
    else:
        print("Priority: LOW")

    print("Recommended Study Day:", study_day)

print("\nAgent has successfully created your study recommendations!")