from teacher import Teacher
from exam_simulator import Exam


teacher = Teacher()

student_view, answers = teacher.create_full_test()

exam = Exam(student_view, answers, store_test=True, topic=teacher.test )

student_answers = exam.take()
print(student_answers)
grade = exam.grade(student_answers)
print(grade)