#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept one number for user and check whether number is prime or not

 ##################################################################################################
#Algorithm
#Start 
#Accept number from user as no
#Display number is prime or not
##End

 ####################################################################################################
#Function Name: CheckPrime()
#input :Integer
#output:integer
#Description:Display  number is prime or not
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def CheckPrime(no):
     for i in range(2,no):
        if(no%i==0):
            print("{} is not prime number".format(no))
            break
        else:
             print("{} is  prime number".format(no))
       
def main():
    value=int(input("Enter any Number:"))
    CheckPrime(value)
    
    
if __name__ == "__main__":
    main()



