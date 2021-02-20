#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # Take one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

 ##################################################################################################
#Algorithm
#Start 
#Accept One number as no1
#if no1 is divisible by 5 then
#no1 is True otherwise
#no1 is False
##End

 ####################################################################################################
#Function Name: DivisibleNumber()
#input :Integer
#output:Integer
#Description: display number True or False
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def DivisibleByNumber(no1):
    if no1%5==0:
        print("Number is True")
    else:
        print("Number is False")
        
       
def main():
    print("Enter number:")
    value=int(input())
    DivisibleByNumber(value)
      
if __name__ == "__main__":
    main()



