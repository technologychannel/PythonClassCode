name = "   harry sharma harry"
names = "hari,shyam,rita"
print(name.upper())
print(name.lower())
#print(f"{name.split(" ")[0].capitalize()} {name.split(" ")[1].capitalize()}")
print(name.title())
print(name.strip())
print(name.replace("harry", "suman"))
lists = names.split(",")


for n in lists:
    print(n)

