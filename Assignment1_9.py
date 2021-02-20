#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # display first 10 even numbers on screen

 ##################################################################################################
#Algorithm
#Start 
#accespt number from user as no1
#
#display first 10 even numbers on screen
#
##End

 ####################################################################################################
#Function Name: DisplayEven()
#input :Integer
#output:Integer
#Description:display first 10 even numbers on screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def DisplayEven(no1):
    icnt=0
    for icnt in range(1,no1*2+1):
        if icnt%2==0:
            print(icnt)
       
       
def main():
    print("Enter number:")
    value=int(input())
    
    DisplayEven(value)
      
if __name__ == "__main__":
    main()



