#Create a Python program that is able to calculate remainder. Remainder can be calculated 
#using modulo “%” operator. See also “modulus” example in W3Schools.

#Prompt user “Insert an integer: ” and assign the input value into Feed variable
Feed = input("Insert an integer: ")
#Convert the Feed into an integer and assign it to Value variable
Value = int(Feed)
#Calculate the remainder of the Value when divided by 2 and assign it to the Remainder variable.
Remainder = Value % 2
#Print the inserted value “Value is {Value}”
print("Value is", Value)
#Print the remainder value “The remainder is {Remainder} when {Value} is divided by 2.”
print("The remainder is", Remainder, "when", Value, "is divided by 2.")

#Example program run:

#Insert an integer: 479
#Value is 479
#The remainder is 1 when 479 is divided by 2.