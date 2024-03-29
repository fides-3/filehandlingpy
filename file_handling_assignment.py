#filecreation
try:
    #crating a new text file in write mode
    with open("my_file.txt","w") as  file:
        file.write("This is line 1\n")
        file.write("12345\n") #writing a string of lines and numbers
        file.write("i am a developer\n")
    print("File created and initial content written successfully.") 
except IOError as e:
    print(f" An error occurred while creating the file:{e}") 
finally:
    print("file creation process completed.")
try:
    with open ("my_file.txt","r")  as file:
        file_content=file.read ()  
        print("\ncontents of my_file.txt:") 
        print(file_content)
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("permission denied to open the file.")  
finally:
    print("File reading process completed.") 

try:
    with open ("my_file.txt","a") as file:
        file.write("i'm 19 years\n")
        file.write("907654\n")
        file.write("i'm a student\n")
    print("\ncontent appendedto my_file.txt successfully.")  
except IOError as e:
    print(f"An error occurred while appending to the file:{e}") 
finally:
    print("File appending proceess completed.")     


