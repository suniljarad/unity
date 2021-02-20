#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # Take one function named as ChkNum() which accept one parameter as number. 
    # If number is even then it should display “Even number” otherwise display “Odd number” on console.

 ##################################################################################################
#Algorithm
#Start 
#Accept one parameter as no1
#Display no1 as Even number or Odd number
#End

 ####################################################################################################
#Function Name: ChkNum()
#input :Integer
#output:Integer
#Description: It should display “Even number” otherwise display “Odd number” on console.
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def ChkNum(no1):
    if no1%2==0:
        return True
    else:
        return False

       
def main():
    print("Enter number:")
    value=int(input())
    
    ret=ChkNum(value)
    
    if ret==True:
        print("{} is Even number".format(value))
    else:
        print("{} is Odd number".format(value))
        

if __name__ == "__main__":
    main()



