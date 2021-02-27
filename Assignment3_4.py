#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # Accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

 ##################################################################################################
#Algorithm
#Start 
#Accept N numbers from user as no
#Display frequency of that number from List
##End

 ####################################################################################################
#Function Name: 
#input :Integer
#output:integer
#Description:Display frequency of that number from List
#Author: Sunil Bhagwan Jarad
#Date:25/2/2021
 ####################################################################################################
       
def main():
   arr=[]
   
   print("Enter how many elements you want:")
   n=int(input())
   
   print("Enter the elements of array:")
   for i in range(0,n):
     no=int(input())
     arr.append(no)
   print("Entered array Elements:",arr) 
   
   
   print("Element to search:")
   num=int(input())
   count=0
   for j in arr:
        if(j==num):
            count=count+1
   print("Frequency of {} is {} times".format(num,count))   
          
if __name__ == "__main__":
   main()



