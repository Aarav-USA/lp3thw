from sys import argv

script, filename = argv

txt = open(ex15_sample.py)

print(f"Here is your file {filename}:")
print(txt.file())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
