#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    #Display multiplication  using Lambda function
 ##################################################################################################
#Algorithm
#Start 

##End

 ####################################################################################################
#Function Name: Lambda function
#input :Integer
#output:integer
#Description:Display multiplication  using Lambda function
#Author: Sunil Bhagwan Jarad
#Date:4/3/2021
 ####################################################################################################

mult=lambda n1,n2:n1*n2
    
def main():
    print("Enter First number")
    value1=int(input())
    
    print("Enter Second number")
    value2=int(input())
    Ret=mult(value1,value2)
    print("Multiplication of two numbers are:",Ret)
    
if __name__ == "__main__":
    main()