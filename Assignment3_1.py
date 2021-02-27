#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept N numbers from user and store it into List. Return addition of all elements from that List.

 ##################################################################################################
#Algorithm
#Start 
#Accept N numbers from user as no
#Display addition of all elements from that List
##End

 ####################################################################################################
#Function Name:Addition()
#input :Integer
#output:integer
#Description:Display addition of all elements from that List
#Author: Sunil Bhagwan Jarad
#Date:25/2/2021
 ####################################################################################################
 
def Addition(List):
    sum=0
    for i in range(len(List)):
        sum=sum+List[i]
    return sum
    
       
def main():
   arr=[]
   num=int(input("Enter how many elements you want:"))
   print("Enter the numbers in array")
    # Iterate the for loop to accept N numbers
   for i in range(0,num):
        # Accept indivisual element from user
    no=int(input())
        # Insert that element into List
    arr.append(no)
   print("Entered elements are:",arr)    
    #print("Sum of digit:",no)
   ret=Addition(arr)
   print("Addition of array elements:",ret)
    
    
    
if __name__ == "__main__":
    main()



