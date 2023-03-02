#### Chiyo Miyake
#### 2023.03.01
#### IT FDN 110 A
#### Assignment 07
# Assignment 07: Examples of Pickling and Exception Handling

## Introduction
In this assignment, we learn about pickling and exception handling, also known as error handling. 
## Pickling
Pickling is a way of converting data into binary format. The binary format is a way to obscure the file content and reduce the size of the file. To use this method of formatting data, you first import the function (Figure 1).

![Picture1](https://user-images.githubusercontent.com/115480796/222325837-f2cb20f0-8d7d-433b-9242-17516b0dc0b5.png)

<sub>Figure 1: Importing the pickling function into our code.</sub>

We can then create some data by obtaining some user inputs and store that into a list (Figure 2).

![Picture2](https://user-images.githubusercontent.com/115480796/222325865-b2602d50-f066-4399-ac09-226eacb62a15.png)

<sub>Figure 2: Creating a list with user input data.</sub>

We then use the pickle.dump() function to ‘dump’, or store the data into a file (Figure 3).
 
![Picture3](https://user-images.githubusercontent.com/115480796/222325889-9bc65b28-493c-402b-8569-9156b2abe895.png)

<sub>Figure 3: Using the built in function pickle.dump() to record data.</sub>

We can read the data by using the pickle.load() function to read one row of data (Figure 4). 

![Picture4](https://user-images.githubusercontent.com/115480796/222325906-572233a6-a183-449f-b59d-6b246f3dbf80.png)

<sub>Figure 4: Reading one line of data in the file.</sub>

When we run the code, the output shows us the list before it gets pickled, and outputs the single row of data in the data file (Figure 5).

![Picture5](https://user-images.githubusercontent.com/115480796/222325922-9a05ab78-39e2-42e8-a4ed-8a30ddb7ac14.png)

<sub>Figure 5: Output of the Pickling Example.</sub>

In the text file, it will show the user input as obscure data (Figure 6).
 
![Picture6](https://user-images.githubusercontent.com/115480796/222325987-0f22c7aa-0278-4852-b1bf-671a902201d2.png)

<sub>Figure 6: Text file with the user data.</sub>

## Exception Handling
I struggled with the exception handling part of this assignment, so I did my best to use the example from the module to help guide me through understanding it. In exception handling, it helps to organize our errors in the code by streamlining what information we want to know. The first part of the exception handling is the ‘try’ block where we try the code by asking for a user input (Figure 7). If the user inputs an alpha-numeric title, it will ‘raise’ the error tell the user to not add numbers into the title. The next ‘raise’ exception is if the user fails to add the file format as ‘.txt.

 ![Picture7](https://user-images.githubusercontent.com/115480796/222325992-5b86f577-8354-47f3-aaa7-99c7af070817.png)

<sub>Figure 7: Try block with raising specific errors.</sub>

When we make the title alpha-numeric, the program will print the error information (Figure 8).
 
 ![Picture8](https://user-images.githubusercontent.com/115480796/222326009-c8cd6af6-212f-406c-b515-9a5182cc442e.png)

<sub>Figure 8: User error, added alpha-numeric title as file.</sub>

When we successfully create a text file with alphabetic characters, the program creates a new text file (Figure 9).
 
 ![Picture9](https://user-images.githubusercontent.com/115480796/222326017-008a431a-fb58-4bc0-ad3a-87424c9b3732.png)

<sub>Figure 9: Successful program.</sub>

We can run both examples on the command prompt (Figure 10). Since the last task to be added to the data file was the Homework task, it will read the first line of the data. And for our exception handling example, this time the error that is raised when creating a new file is not specifying the file type as a text file.
 
 ![Picture10](https://user-images.githubusercontent.com/115480796/222326036-3b36526a-e2d1-43c2-8514-61704d65b30a.png)

<sub>Figure 10: Running the examples in the command prompt.</sub>

## Summary
In summary, pickling is a good way of condensing file size by obscuring the file data into a binary format. Exception handling is also a good way of managing the errors in a program. Instead of making a user read the complex debugging messages, we can organize and format the specific errors we want to keep track of.
