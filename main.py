def analyze_student_performance(student_scores, threshold):
    if student_scores is None or len(student_scores) == 0:
        return "No student data available"

    weak_count = 0
    total_score= 0;

    for score in student_scores:
        if score < 0 or score > 100:
            print("Invalid score")
            continue

        total_score += score

        if score >= threshold:
            weak_count += 1
        else:
            pass

    average_score = total_score / len(student_scores)

    if weak_count > 2:
        performance_status = "Student has weak academic areas"
    elif average_score < threshold:
        performance_status = "Overall performance is below average"
    else:
        performance_status = "Student performance is acceptable"

    return performance_status

# sample scores
scores = [45, 55, 70, 40, 90]
threshold = 50

result = analyze_student_performance(scores, threshold)
print("Analysis Result:", result)
