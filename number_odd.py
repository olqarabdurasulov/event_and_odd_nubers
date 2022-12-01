#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 5975
#Print the number of odd digits in the variable "var_int".
a = var_int%10
b = var_int//10%10
c = var_int//100%10
d = var_int%1000
print((a)%2 + (b)%2 + (c)%2 + (d)%2)