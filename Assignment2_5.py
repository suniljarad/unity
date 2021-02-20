#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept one number form user and return addition of its factors.

 ##################################################################################################
#Algorithm
#Start 
#Accept number from user as no
#Display addition of factors
##End

 ####################################################################################################
#Function Name: AddFactor()
#input :String
#output:integer
#Description:Display Display addition of factors
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def AddFactor(no):
    for i in range(1,no+1):
        if(no%i==0):
            print(i)
        
    
       
def main():
   value=int(input("Enter any Number:"))
   AddFactor(value)
      
if __name__ == "__main__":
    main()



