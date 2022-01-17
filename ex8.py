# set formatter to 4 closed brackets
formatter = "{} {} {} {}"

# prints 4 closed brackets and formats 1-4
print(formatter.format(1, 2, 3, 4))
# prints 4 closed brackets and formats one-four
print(formatter.format("one", "two", "three", "four"))
# prints 4 closed brackets and formats true or false
print(formatter.format(True, False, False, True))
# prints 4 closed brackets per variable (16)
print(formatter.format(formatter, formatter, formatter, formatter))
# prints 4 closed brackets and formats text
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
