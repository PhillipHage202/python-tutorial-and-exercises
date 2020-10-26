
student_name = input("Enter Name: ")
student_homework = int (input("Enter homework /25: "))
student_assessment = int (input("Enter assessment /50: "))
student_final_exam = int (input("Enter final exam /100: "))

def grade_calc (anme, homework, assessment, final_exam):
    if homework >25 or assessment > 50 or final_exam >100:
        return "invalid number"
    total = homework + assessment + final_exam
    grade = (total / 1750 ) * 1000
    return grade
    

grade = grade_calc(student_name,student_homework, student_assessment, student_final_exam)

print (f"{student_name}, Your Final Mark is: {grade}%" )