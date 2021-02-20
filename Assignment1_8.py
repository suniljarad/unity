#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept number from user and print that number of “*” on screen

 ##################################################################################################
#Algorithm
#Start 
#Accept number  as no1
#Display * on Screen
##End

 ####################################################################################################
#Function Name: DisplayStar()
#input :Integer
#output:string
#Description: display number of "*" on screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def DisplayStar(no1):
    icnt=0
    for icnt in range(0,no1):
        print("*")
       
def main():
    print("Enter number:")
    value=int(input())
    
    DisplayStar(value)
    
      
if __name__ == "__main__":
    main()



