n = int(input())

grades = []

for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)


def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 35:
            A = grades[i]%5
            if A == 3:
                A1 = str (grades[i]+A - 1)
                print(A1)

            elif A == 4:
                A2 = str (grades[i]+A - 1)
                print(A2)

            else :
                print(grades[i])
        else:
            A3 = str (grades[i])
            print(A3)

result = gradingStudents(grades)