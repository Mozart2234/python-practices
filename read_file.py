# with open("./story.txt", "r", encoding="utf-8") as f:
#     for lines in f:
#         print(lines, end="")

# with open("./story.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines)
#

# with open("./story.txt", "a") as file:
#     file.write("\nThis is a new line\n")
#

with open("./story.txt", "w") as file:
    file.write("Rewriting the file\n")
    file.write("Bye Bye!!\n")
