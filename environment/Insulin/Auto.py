import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("File does not exists. File needs to be created.")

f = open("file.txt", "w+").write("Overwrite a file in Python.")

f = open("file.txt", "r")
print(f.read())
f.close()