# Variables representing library data
total_books = 500 # int
average_rating = 4.5 # float
librarian_name = "John Doe" # str
is_open = True # bool
book_names = ["Python Programming", "Introduction to Data Science",
"History of Art"] # list
location_coordinates = (40.7128, -74.0060) # tuple (latitude,
contact_details = {
"phone": "123-456-7890",
"email": "library@example.com",
"address": "123 Library St, City, State"
} # dict
unique_genres = {"Fiction", "Non-fiction", "Science Fiction"} # set
# Printing out the library information
print("Library Information:")
print(f"Total number of books: {total_books}")
print(f"Average book rating: {average_rating}")
print(f"Librarian's name: {librarian_name}")
print(f"Is library open?: {'Yes' if is_open else 'No'}")
print(f"List of book names available: {book_names}")
print(f"Location coordinates: {location_coordinates}")
print(f"Contact details: {contact_details}")
print(f"Unique genres available: {unique_genres}")