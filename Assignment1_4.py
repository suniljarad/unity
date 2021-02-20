#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # display 5 times Marvellous on screen

 ##################################################################################################
#Algorithm
#Start 
#Accept number of iterations as no1
#Display 5 times Marvellous on Screen
##End

 ####################################################################################################
#Function Name: Display()
#input :Integer
#output:string
#Description: display 5 times Marvellous on screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def Display(no1):
    icnt=0
    for icnt in range(0,no1):
        print("Marvellous")

       
def main():
    print("Enter the number of iterations:")
    value=int(input())
    
    Display(value)
      
if __name__ == "__main__":
    main()



