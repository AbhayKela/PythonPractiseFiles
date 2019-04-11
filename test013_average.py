numbers1=[2,3,4]
numbers2=[5,6]
def average (num1,num2):
    total=sum (num1)+sum(num2)
    total= float (total)
    avg= total/len(num1)+len(num2)
    return avg
print(average(numbers1,numbers2))

print("=================----------------------------------======================")

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

def average (num1,num2,num3):
    total=sum (num1+num2+num3)
    total= float (total)
    avg1= total/(len(num1)+len(num2)+len(num3))
    return avg1

student_list=["lloyd","alice","tyler"]

def get_average(student):
    homework=average(lloyd["homework"],alice["homework"],tyler["homework"])
    quizzes=average(lloyd["quizzes"],alice["quizzes"],tyler["quizzes"])
    tests=average(lloyd["tests"],alice["tests"],tyler["tests"])
    return (0.1*homework) + (0.3*quizzes) + (0.6*tests)
print(get_average (student_list))

print("===================----------------------====================")

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

print(get_average(lloyd))
print(get_average(alice))
print(get_average(tyler))