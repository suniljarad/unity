#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # Take one function named as Add() which accepts two numbers from user and return addition of that two numbers.

 ##################################################################################################
#Algorithm
#Start 
#Accept first number as no1
#Accept second number as no2
#return addition of no1 & no2
#Display Addition  of the user
#End

 ####################################################################################################
#Function Name: Add()
#input :Integer,Integer
#output:Integer
#Description: Perform addition of Two numbers
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def Add(no1,no2):
    ans=no1+no2
    return ans

       
def main():
    print("Enter  first number:")
    value1=int(input())
    print("Enter second number:")
    value2=int(input())
    Ret=Add(value1,value2)
    
    print("Addition of {} and {} is {} ".format(value1,value2,Ret))
    
    

if __name__ == "__main__":
    main()



