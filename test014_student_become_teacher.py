lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
students=[lloyd,alice,tyler]

def average (num):
    total=sum (num)
    total= float (total)
    avg= total/(len(num))
    return avg

def get_average(student):
    homework=average(student["homework"])
    quiz=average(student["quizzes"])
    test= average(student["tests"])
    return 0.1*homework + 0.3*quiz+ 0.6 *test

def get_letter_grade(score) :

    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif  score >= 60 :
        return "D"
    else :
        return "F"

def get_class_average (students) :
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)

print get_class_average(students)
print get_letter_grade(get_class_average(students))