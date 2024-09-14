# No Parameter And No Return Type
def prime_minister():
    print("Current prime minister is Bishworaj")

# prime_minister()

# Parameter And No Return Type
def full_name(first_name, last_name):
    print(f"Full name is {first_name} {last_name}")

# full_name("Bimal", "Sharma")


# Parameter And Return Type
def full_name(first_name, last_name):
    fullname = f"{first_name} {last_name}"
    return fullname


fn = full_name("Rahul", "Sharma")
print(fn)

# No Parameter And Return Type
def voter_age():
    return 18


ram_age = 20
if ram_age >= voter_age():
    print("Ram is voter")
else: 
    print("Ram is not voter")