

# numbers = [x**2 for x in range(1,6)]

# # 1^2 = 1 * 1
# # 2^2 = 2 * 2

# print(numbers)


# Step 1: List of student scores
scores = [65, 85, 90, 78, 88, 92, 56]
# Step 2: Filter out scores above 80 using list comprehension
high_scores = [score for score in scores if score > 80]
print("High Scores:", high_scores)


words = ["apple", "banana", "grape", "kiwi", "peach", "plum"]
# Step 2: Filter words with exactly 5 letters using list comprehension
five_letter_words = [word for word in words if len(word) == 5]
print("Five Letter Words:", five_letter_words)



numbers = [2,4,6,5,7,12]
divide_by_2 = [x for x in numbers if x%2==0]
print(divide_by_2)
