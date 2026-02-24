# ===============================
# 7. TAKE USER INPUT (SAFE VERSION)
# ===============================

print("\nEnter Patient Details:\n")

age = int(input("Age: "))

print("Sex: 0 = Female, 1 = Male")
sex = int(input("Enter 0 or 1: "))

print("Chest Pain Type (0-3)")
chest_pain_type = int(input("Enter value: "))

resting_blood_pressure = int(input("Resting Blood Pressure: "))
cholesterol = int(input("Cholesterol: "))

print("Fasting Blood Sugar: 0 = Lower than 120, 1 = Greater than 120")
fasting_blood_sugar = int(input("Enter 0 or 1: "))

print("Rest ECG (0-2)")
rest_ecg = int(input("Enter value: "))

max_heart_rate = int(input("Max Heart Rate: "))

print("Exercise Induced Angina: 0 = No, 1 = Yes")
exercise_induced_angina = int(input("Enter 0 or 1: "))

oldpeak = float(input("Oldpeak: "))

print("Slope (0-2)")
slope = int(input("Enter value: "))

print("Vessels Colored by Fluoroscopy (0-3)")
vessels_colored_by_flourosopy = int(input("Enter value: "))

print("Thalassemia (0-2)")
thalassemia = int(input("Enter value: "))