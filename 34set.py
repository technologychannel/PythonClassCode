fruits = {'Apple', 'Mango', 'Orange','Apple'}
fruits.add("Banana")


for fruit in fruits:
    print(fruit)


course_A_students = {"Alice", "Bob", "Charlie"}
course_B_students = {"Charlie", "David", "Alice"}
common_students = course_A_students.intersection(course_B_students)
print(common_students)
