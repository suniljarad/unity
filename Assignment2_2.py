#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept one number and display  pattern.

 ##################################################################################################
#Algorithm
#Start 

##End

 ####################################################################################################
#Function Name: DisplayPattern()
#input :Integer
#output:String
#Description:Display Pattern
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def DisplayPattern(no1):
    icnt1=0
    icnt2=0
    for icnt1 in range(0,no1):
        for icnt2 in range(0,no1):
            print("*",end='')
        print()   
    
      
def main():
    print("Enter number:")
    value=int(input())
    
    DisplayPattern(value)
      
if __name__ == "__main__":
    main()



