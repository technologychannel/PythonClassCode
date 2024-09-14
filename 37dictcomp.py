data = {x: x**2 for x in range(1,10)}
print(data)
student_scores = {"Alice": 85, "Bob": 76, "Charlie": 90, "David": 65, "Eve": 88}

more_than_80 = {name: val for name,val in student_scores.items() if val>80}
print(more_than_80)