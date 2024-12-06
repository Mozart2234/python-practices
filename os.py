import os

# obtener el directorio actual
cwd = os.getcwd()
print("The current working directory is:", cwd)

# List .txt files
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print(f"List of .txt files: {txt_files}")

print(os.listdir(cwd))
