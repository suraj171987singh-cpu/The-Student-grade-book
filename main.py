grade_book = {"Shreya" : 92,"Priya" : 89 , "Charul" : 29 , "Vedanshi" : 22 , "Kashish" : 32}
total_score = 0
for score in grade_book.values():
    total_score += score
class_average = total_score/len(grade_book)
print(f"Class average: {class_average}")

top_student = max(grade_book,key=grade_book.get)
highest_score = grade_book[top_student]

bottom_student = min(grade_book,key=grade_book.get)
lowest_score = grade_book[bottom_student]

print(f"Top student: {top_student} with {highest_score}")
print(f"Lowest student: {bottom_student} with {lowest_score}")


search_student = input("\nEnter the name of the student:")
student_marks = grade_book.get(search_student)

if student_marks is None:
    print("Student not found")
else:
    print(f"{search_student} got {student_marks} percentage ")