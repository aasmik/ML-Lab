def candidate_elimination(concepts, target):
    # Initialize Specific and General boundaries
    S = ["Ø"] * len(concepts[0])
    G = [["?"] * len(concepts[0])]

    # Process each training example
    for i, example in enumerate(concepts):

        # Case 1: Positive example
        if target[i] == "Yes":
            for j in range(len(example)):
                if S[j] == "Ø":
                    S[j] = example[j]
                elif S[j] != example[j]:
                    S[j] = "?"

            # Remove inconsistent hypotheses from G
            G = [
                g for g in G
                if all(g[k] == "?" or g[k] == S[k] for k in range(len(example)))
            ]

        # Case 2: Negative example
        else:
            new_G = []
            for g in G:
                if all(g[k] == "?" or g[k] == example[k] for k in range(len(example))):
                    for j in range(len(example)):
                        if S[j] != "?" and S[j] != example[j]:
                            new_h = g.copy()
                            new_h[j] = S[j]
                            new_G.append(new_h)
                else:
                    new_G.append(g)
            G = new_G

        # Print step-by-step output
        print(f"After example {i + 1}")
        print("S =", S)
        print("G =", G)
        print("-" * 40)

    return S, G


# ===================== DATASET (4 ROWS) =====================

# Attributes: Degree, Experience, Skills, Location
concepts = [
    ["BTech", "Senior", "Good", "City"],
    ["BTech", "Junior", "Good", "City"],
    ["BSc", "Junior", "Average", "Town"],
    ["BTech", "Senior", "Good", "Town"]
]

# Target: Yes = Selected, No = Not Selected
target = ["Yes", "Yes", "No", "Yes"]

# ===================== RUN ALGORITHM =====================

S_final, G_final = candidate_elimination(concepts, target)

print("\nFinal Specific Boundary:", S_final)
print("Final General Boundary:", G_final)
