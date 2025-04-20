import numpy as np


np.random.seed(42)  
scores = np.random.randint(40, 100, size=(10, 5))  


avg_per_student = scores.mean(axis=1)
avg_per_subject = scores.mean(axis=0)
class_avg = scores.mean()
highest_score = scores.max()
lowest_score = scores.min()


def assign_grades(avg_scores):
    grades = []
    for score in avg_scores:
        if score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        else:
            grades.append('F')
    return np.array(grades)

grades = assign_grades(avg_per_student)


print("Student Scores (Rows: Students, Columns: Subjects):\n", scores)
print("\n Average Score per Student:\n", avg_per_student)
print("\n Average Score per Subject:\n", avg_per_subject)
print(f"\n Class Average Score: {class_avg:.2f}")
print(f"\n Highest Score in Class: {highest_score}")
print(f" Lowest Score in Class: {lowest_score}")
print("\n Grades per Student:\n", grades)
