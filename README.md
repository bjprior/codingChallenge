The code is run by simply running the body of the main.py file

Considerations when writing this code:
1. I opted to follow an object oriented programing style. I felt this encapsulated the code nicely into a single object, 
Number. I only exposed the necessary methods to the user, namely the constructor and the print method. I could have 
opted to print the writen number directly when instantiating the object however chose to have a public method.
2. I decided to "hide" the functions which are called only from inside the object through the use of an 
'_' in front of the method name.
3. The maximum integer size is set to 999999999999999999. This can be extended by adding the relevant english text 
in the "Thousands" dictionary and updating the MAXINTEGER global variable.
4. Possible extensions to code code could include: 
- Extension for negative numbers 
- Extension for decimals,
- Multiple numbers in the string
5. I have assumed: 
- A number with a unit immediately preceding is an invalid number ie 800g
- Each line ends with a full stop