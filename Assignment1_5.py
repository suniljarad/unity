#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # display 10 to 1 on screen

 ##################################################################################################
#Algorithm
#Start 
#display 10 to 1 on screen
##End

 ####################################################################################################
#Function Name: Display()
#input :Integer
#output:integer
#Description: display 10 to 1 on screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
def Display():
    print("start output")
    icnt=0
    for icnt in range(10,1,-1):
        print(icnt)
    else:
        print("End output")
       
def main():
    Display()
      
if __name__ == "__main__":
    main()



