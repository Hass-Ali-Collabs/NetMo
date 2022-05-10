'''
Notes:

Read Only (‘r’) : Open text file for reading. The handle is
positioned at the beginning of the file. If the file does not exists, 
raises I/O error. This is also the default mode in which file is opened.

Read and Write (‘r+’) : Open the file for reading and writing. 
The handle is positioned at the beginning of the file. Raises I/O error 
if the file does not exists.

Append and Read (‘a+’) : Open the file for reading and writing. 
The file is created if it does not exist. The handle is positioned at 
the end of the file. The data being written will be inserted at the end, 
after the existing data.
'''

# the command :  
# to read file : File_object = open(r"File_Name", "Access_Mode")
#to close the file: File_object.close()

#============================================================
#code example:


# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 
file1 = open("MyFile.txt", "r") 
    
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file2 = open(r"D:/Text/MyFile2.txt", "r+") 


# Opening and Closing a file "MyFile.txt" 
# for object name file1. 
file1 = open("MyFile.txt", "r") 
file1.close() 


#==============================================================


'''
read() : Returns the read bytes in form of a string. Reads n bytes, 
if no n specified, reads the entire file.

File_object.read([n])

readline() : Reads a line of the file and returns in form of a string.
For specified n, reads at most n bytes. However, does not reads more 
than one line, even if n exceeds the length of the line.

File_object.readline([n])

readlines() : Reads all the lines and return them as each line a string 
element in a list.

File_object.readlines()

'''

#example:

# Program to show various ways to 
# read data from a file. 
  
# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
  
# Writing data to a file
file1.write("Hello \n") 
file1.writelines(L)
file1.close()  # to change file access modes
  
file1 = open("myfile.txt", "r+")
  
print("Output of Read function is ")
print(file1.read())
print()
  
# seek(n) takes the file handle to the nth
# bite from the beginning. 
file1.seek(0)
  
print("Output of Readline function is ")
print(file1.readline())
print()
  
file1.seek(0)
  
# To show difference between read and readline 
print("Output of Read(9) function is ")
print(file1.read(9))
print()
  
file1.seek(0)
  
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
  
file1.seek(0)
  
# readlines function 
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close() 

'''
output

Output of Read function is
Hello
This is Delhi
This is Paris
This is London


Output of Readline function is
Hello


Output of Read(9) function is
Hello
Th

Output of Readline(9) function is
Hello


Output of Readlines function is
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n']
'''
#===================================================================

