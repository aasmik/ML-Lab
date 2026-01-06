# Naive Bayes from Scratch - Study Readiness Classification

# Training data
data = [
    ("I revised all chapters", "Ready"),
    ("Practiced previous year questions", "Ready"),
    ("Notes are completed", "Ready"),
    ("Confident about the syllabus", "Ready"),
    ("Mock tests completed", "Ready"),
    
    ("Did not understand last class", "Not Ready"),
    ("Feeling sleepy and distracted", "Not Ready"),
    ("No preparation done", "Not Ready"),
    ("Haven't opened the book yet", "Not Ready"),
    ("Too stressed to study", "Not Ready")
]

# Step 1: Separate data by class
ready_texts = []
not_ready_texts = []

for text, label in data:
    if label == "Ready":
        ready_texts.append(text.lower().split())
    else:
        not_ready_texts.append(text.lower().split())

# Step 2: Calculate prior probabilities
total_docs = len(data)
P_ready = len(ready_texts) / total_docs
P_not_ready = len(not_ready_texts) / total_docs

# Step 3: Build vocabulary
vocab = set()
for text, _ in data:
    vocab.update(text.lower().split())

vocab_size = len(vocab)

# Step 4: Count word frequencies
from collections import defaultdict

ready_word_count = defaultdict(int)
not_ready_word_count = defaultdict(int)

for text in ready_texts:
    for word in text:
        ready_word_count[word] += 1

for text in not_ready_texts:
    for word in text:
        not_ready_word_count[word] += 1

total_ready_words = sum(ready_word_count.values())
total_not_ready_words = sum(not_ready_word_count.values())

# Step 5: Prediction function with Laplace smoothing
def predict(sentence):
    words = sentence.lower().split()
    
    prob_ready = P_ready
    prob_not_ready = P_not_ready
    
    for word in words:
        prob_ready *= (ready_word_count[word] + 1) / (total_ready_words + vocab_size)
        prob_not_ready *= (not_ready_word_count[word] + 1) / (total_not_ready_words + vocab_size)
    
    if prob_ready > prob_not_ready:
        return "Ready"
    else:
        return "Not Ready"

# Step 6: Test the model
test_sentence = "completed mock tests"
result = predict(test_sentence)

print("Test Sentence:", test_sentence)
print("Prediction:", result)