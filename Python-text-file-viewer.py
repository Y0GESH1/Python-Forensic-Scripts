import os 
def file_view(file):
    try:
        abs_path = os.path.abspath(file_path)
        with open(file_path,'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("erro reading file")

file_path =  input("Enter the file to a path :")
file_view(file_path)
