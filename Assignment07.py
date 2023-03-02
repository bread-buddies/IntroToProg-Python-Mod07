# .........................................#
# Title: Assignment07 - Examples of Pickling and Exception Handling
# Desc: Python script
# Change Log: (Who, When, What)
# CMiyake,2023-02-27,Created File
# .........................................#

import pickle  # This imports code from another code file!

strTask = str(input("Enter a task: "))
strPriority = str(input("What is the priority? "))
lstTask = [strTask, strPriority]
print(lstTask)

# Now we store the data with the pickle.dump method
objFile = open("datafile.dat", "ab")
pickle.dump(lstTask, objFile)
objFile.close()

# And, we read the data back with the pickle.load method
objFile = open("datafile.dat", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
objFile.close()
print(objFileData)

# Example of exception handling
try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isalnum():
        raise Exception('Do not use numbers for the file\'s name')
    elif new_file_name.endswith('txt') == False:
        raise FileNotTXTError()

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

