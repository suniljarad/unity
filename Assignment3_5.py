#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    #Accept N numbers from user and store it into List. 
    #Return addition of all prime numbers from that List. 
    #Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named asMarvellousNum.
    #Name of the function from main python file should be ListPrime().
 ##################################################################################################
#Algorithm
#Start 

##End

 ####################################################################################################
#Function Name: DisplaySumDigit()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:25/2/2021
 ####################################################################################################
import MarvellousNum


def ListPrime(List):
    
    
    print("prime Number List:",prime)



def main():
    arr=[]
    n=int(input("Enter how many number of elements:"))
    print("Enter the array elements:")
    for i in range(0,n):
        no=int(input())
        arr.append(no)
    print("Entered array elements are:",arr)
    MarvellousNum.ChkPrime(arr)
    
    #ListPrime(arr)
    
if __name__ == "__main__":
    main()