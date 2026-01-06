logs = [
    ["S101", "Asha", "LOGIN", "2025-03-10"],
    ["S101", "Asha", "LOGIN", "2025-03-10"],
    ["S102", "Ravi", "SUBMIT", "2025-03-10"],
    ["S101", "Asha", "LOGOUT", "2025-03-10"],
    ["S103", "Meena", "LOGIN", "2025-03-11"]
]

student_counts = {}
login_status = {}     
daily_counts = {}     

for log in logs:
    sid, name, activity, date = log

    if sid not in student_counts:
        student_counts[sid] = {"name": name, "LOGIN": 0, "SUBMIT": 0}

    if activity == "LOGIN":
        student_counts[sid]["LOGIN"] += 1
        login_status[sid] = login_status.get(sid, 0) + 1
    elif activity == "SUBMIT":
        student_counts[sid]["SUBMIT"] += 1
    elif activity == "LOGOUT":
        login_status[sid] = max(login_status.get(sid, 0) - 1, 0)

    daily_counts[date] = daily_counts.get(date, 0) + 1

print("STUDENT ACTIVITY REPORT\n")
for sid, data in student_counts.items():
    print(f"{sid} | {data['name']} | Logins: {data['LOGIN']} | Submissions: {data['SUBMIT']}")

print("\nABNORMAL BEHAVIOR REPORT")
for sid, count in login_status.items():
    if count > 0:
        print(f"{sid} has multiple logins without logout")

print("\nDAILY ACTIVITY STATISTICS")
for date, count in daily_counts.items():
    print(f"{date}: {count} activities")

