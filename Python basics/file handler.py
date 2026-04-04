#file handler


# Open file using context manager - No need to explicitly close the file, context manager handles it
with open(r"C:\Users\admin\Downloads\File_handling_test.txt", "r") as f:
    # Check if file is readable
    print("Is file readable:", f.readable())
    
    # Print file properties
    print("File name:", f.name)
    print("File mode:", f.mode)
    
    # Read and print content
    content= f.read(4)
    print("File content:", content)
    print(f.tell()) # Print current file pointer position
    print(f.seek(0)) # Move file pointer to the beginning
    content = f.read()
    print("File content:", content)
    f.seek(0)
    #to read line by line
    print(f.readline())  # Read and print first line
    print(f.readline())  # Read and print second line
    f.seek(0)
    # Print each line in the file
    for line in f:
        print("Line:", line.strip()) 
    f.seek(0)
    #to readlines
    lines = f.readlines()
    print("All lines:", lines) # return lines as list
#write mode
h=open(r"C:\Users\admin\Downloads\File_handling_test.txt1", "w")
h.write("This is a new file created using write mode.\n")
h.tell()
h.seek(0)
print("Is file readable:", h.readable()) #it will return false as file is opened in write mode
h.close()
##############################################
#in interative mode, if u write something it will not be saved until u close the file or flush the buffer
m=open(r"C:\Users\admin\Downloads\File_handling_test.txt1", "w")
m.write("This is another line in the file.\n") 
m.flush()  # Flush the buffer to ensure data is written to the file
m.close()
##################################################
#append mode
k=open(r"C:\Users\admin\Downloads\File_handling_test.txt1", "a")
k.write("This line is appended to the file.\n")
print("a Is file readable:", k.readable()) #it will return false as file is opened in append mode
k.close()
#read and write mode
p=open(r"C:\Users\admin\Downloads\File_handling_test.txt1", "r+")
print("r+ Is file readable:", p.readable())
print(p.read()) # Read and print existing content   
p.close()
#append and read mode
q=open(r"C:\Users\admin\Downloads\File_handling_test.txt1", "a+")
print("a+ Is file readable:", q.readable())  
print(q.closed) #to check is filed is closed or not
q.close()
#reading image file
with open(r"C:\Users\admin\Downloads\1471797.jpg", "rb") as f:
   img= f.read() # Read and print binary content of the image file
   with open(r"C:\Users\admin\Downloads\imagetest.jpg", "wb") as f1: 
         f1.write(img)  # Write binary content to a new image file
#writelines   
A =['Hai', 'Hello', 'Welcome', 'To', 'File', 'Handling']
with open(r"C:\Users\admin\Downloads\File_handling_test2.txt", "w") as f2:
    f2.writelines("%s\n" % line for line in A)  # Write list of strings to file, each on a new line