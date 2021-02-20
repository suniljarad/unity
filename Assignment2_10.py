#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept number from user and return addition of digits in that number

 ##################################################################################################
#Algorithm
#Start 
#Accept number from user as no
#Display addition of digit number
##End

 ####################################################################################################
#Function Name: DisplaySumDigit()
#input :Integer
#output:integer
#Description:Display addition of digit number
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def DisplaySumDigit(no):
    sum=0
    while(no!=0):
        sum=sum+int(no%10)
        no=int(no/10)
    return sum
    #print(DisplaySumDigit(no))
       
def main():
    value=int(input("Enter any Number:"))
    no=DisplaySumDigit(value)
    print("Sum of digit:",no)
    
if __name__ == "__main__":
    main()



