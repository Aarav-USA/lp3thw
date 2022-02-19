# prompt for input function
prompt = ">>> "
# print context for input
print("What filepath should I open?")
# input prompt; context line 4
filename = input(prompt)
# open file from prompt/input
txt = open(filename)

# print file argument context
print(f"Here's your file {filename}:")
# print file content
print(txt.read())

txt.close()