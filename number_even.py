#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 6754
#Print the number of even digits in the variable "var_int".
a = var_int%10
b = var_int//10%10
c = var_int//100%10
d = var_int%1000
print((a+1)%2 + (b+1)%2 + (c+1)%2 + (d+1)%2)


