#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # Accept number from user and check whether that number is positive or negative or zero.

 ##################################################################################################
#Algorithm
#Start 
#Accept number  as no1
#Display Number is positive or negative or zero
#End

 ####################################################################################################
#Function Name: CheckNumber()
#input :Integer
#output:Integer
#Description: Display Number is positive or negative or zero
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def CheckNumber(no1):
    if no1>0:
        print("Number is positive")
    elif(no1<0):
        print("Number is negative")
    else:
        print("Number is zero")
          
def main():
   print("Enter Any number")
   num=int(input())
   CheckNumber(num)
        
if __name__ == "__main__":
    main()



