import os

try:
    os.rmdir("myfolder")
    print("Folder deleted successful")
except:
    print("Folder not found")


