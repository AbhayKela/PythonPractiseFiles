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

def average (num):
    total=sum (num)
    total= float (total)
    avg1= total/(len(num))
    return avg1

def get_average(student):
    homework=average(student["homework"])
    quiz=average(student["quizzes"])
    test= average(student["tests"])

    return 0.1*homework + 0.3*quiz+ 0.6 *test
get_average_lloyd=get_average(lloyd)
get_average_alice=get_average(alice)
get_average_tyler=get_average(tyler)

print get_average(lloyd)
print get_average(alice)
print get_average(tyler)

def get_letter_grade(score):
    if score>=90:
        return "A"
    elif 90>score>=80:
        return "B"
    elif 80>score>=70:
        return "C"
    elif 70>score>=60:
        return "D"
    else:
        return "F"
print get_letter_grade(get_average_lloyd)
print get_letter_grade(get_average_alice)
print get_letter_grade(get_average_tyler)
