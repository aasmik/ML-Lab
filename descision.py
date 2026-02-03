import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_text


# -----------------------------
# Dataset
# -----------------------------
data = [
    {"Idea": "High", "Teamwork": "Good", "Presentation": "Strong", "Won": "Yes"},
    {"Idea": "High", "Teamwork": "Good", "Presentation": "Average", "Won": "Yes"},
    {"Idea": "High", "Teamwork": "Poor", "Presentation": "Strong", "Won": "Yes"},
    {"Idea": "Medium", "Teamwork": "Good", "Presentation": "Strong", "Won": "Yes"},
    {"Idea": "Medium", "Teamwork": "Poor", "Presentation": "Average", "Won": "No"},
    {"Idea": "Medium", "Teamwork": "Good", "Presentation": "Weak", "Won": "No"},
    {"Idea": "Low", "Teamwork": "Good", "Presentation": "Strong", "Won": "No"},
    {"Idea": "Low", "Teamwork": "Poor", "Presentation": "Average", "Won": "No"},
    {"Idea": "Low", "Teamwork": "Good", "Presentation": "Weak", "Won": "No"},
    {"Idea": "Low", "Teamwork": "Poor", "Presentation": "Weak", "Won": "No"}
]

df = pd.DataFrame(data)

print("ORIGINAL DATASET:\n")
print(df)


# -----------------------------
# Label Encoding
# -----------------------------
le_idea = LabelEncoder()
le_teamwork = LabelEncoder()
le_presentation = LabelEncoder()
le_won = LabelEncoder()

df['Idea'] = le_idea.fit_transform(df['Idea'])
df['Teamwork'] = le_teamwork.fit_transform(df['Teamwork'])
df['Presentation'] = le_presentation.fit_transform(df['Presentation'])
df['Won'] = le_won.fit_transform(df['Won'])

print("\nENCODED DATASET:\n")
print(df)


# -----------------------------
# Feature & Target
# -----------------------------
X = df[['Idea', 'Teamwork', 'Presentation']]
y = df['Won']


# -----------------------------
# Train Decision Tree
# -----------------------------
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)


# -----------------------------
# Decision Tree Structure
# -----------------------------
print("\nDECISION TREE STRUCTURE:\n")
tree_rules = export_text(
    model,
    feature_names=['Idea', 'Teamwork', 'Presentation']
)
print(tree_rules)


# -----------------------------
# Prediction for New Instance
# -----------------------------
idea_input = le_idea.transform(['High'])[0]
teamwork_input = le_teamwork.transform(['Good'])[0]
presentation_input = le_presentation.transform(['Weak'])[0]

new_data = [[idea_input, teamwork_input, presentation_input]]
prediction = model.predict(new_data)

result = le_won.inverse_transform(prediction)

print("\nNEW INSTANCE PREDICTION:")
print("Idea = High")
print("Teamwork = Good")
print("Presentation = Weak")
print("Predicted Result =", result[0])
