#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept name from user and display length of its name.

 ##################################################################################################
#Algorithm
#Start 
#Accept name from user as name
#Display length of given name on Screen
##End

 ####################################################################################################
#Function Name: Display()
#input :String
#output:integer
#Description:Display length of given name on Screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def Display(name):
    print(len(name))
    
       
def main():
   name=input("Enter the any name:")
   Display(name)
      
if __name__ == "__main__":
    main()



