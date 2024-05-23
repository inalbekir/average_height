# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_ = 0
for height in student_heights:
    sum_ += height

total_students = 0
for students in student_heights:
    total_students += 1

average_height = sum_ / total_students

average_height = (round(average_height))

print(f"total height = {sum_}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")