#определение Pass/Fall
scores = [65, 90, 45, 80, 50, 76, 88, 92, 59, 30]
result = []


for score in scores:
    if score >= 60:
        result.append("PASS")
    else:
        result.append("FAIL")


for i in range(len(scores)):
    print(f"score: {scores[i]} -> {result[i]}")
