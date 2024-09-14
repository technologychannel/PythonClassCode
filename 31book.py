books = ["Book A", "Book B", "Book C", "Book D"]
for book in books:
    if book == "Book C":
        print("Found the book! Stopping search.")
        break   
    print(f"Checking {book}")
print("Search ended.")