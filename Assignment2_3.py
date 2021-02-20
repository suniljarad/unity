#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept one number from user and return its factorial.

 ##################################################################################################
#Algorithm
#Start 
#Accept one number from user as no
#Display Factorial of that number on screen
##End

 ####################################################################################################
#Function Name: Factorial()
#input :Integer
#output:integer
#Description:Display Factorial of number on screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def Factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    print("Factorial No is:",fact)
    
    
       
def main():
    value=int(input("Enter the Number:"))
    Factorial(value)
      
if __name__ == "__main__":
    main()



