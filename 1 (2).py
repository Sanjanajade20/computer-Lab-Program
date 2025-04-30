# Write a program that receives an integer an input. If a string is entered instead
# of an integer, then report an error and give another chance to user to enter an 
# integer. Continue this process till correct input is supplied.

while True:
    try:
        # Take input from the user
        user_input = input("Please enter an integer: ")
        
        # Try converting the input to an integer
        num = int(user_input)
        
        # If conversion is successful, break the loop
        print(f"Thank you! You entered the integer: {num}")
        break
    except ValueError:
        # If an error occurs (ValueError), print an error message
        print("Error! That's not a valid integer. Please try again.")
