#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
    # accept N numbers from user and store it into List. Return Maximum/Minimum number from that List.

 ##################################################################################################
#Algorithm
#Start 
#Accept N numbers from user as no
#Display Maximum or minimum number from that List
##End

 ####################################################################################################
#Function Name: Max(),min()
#input :Integer
#output:integer
#Description:Display Maximum or minimum number from that List
#Author: Sunil Bhagwan Jarad
#Date:25/2/2021
 ####################################################################################################
 
def Max(List):
    max=List[0]
    for i in range(0,len(List)):
        if(List[i]>max):
            max=List[i]
    return max
    
def Min(List):
    min=List[0]
    for i in range(0,len(List)):
        if(List[i]<min):
            min=List[i]
    return min
     
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
     
   MaxNumber=Max(arr)
   print("Maximum Number is:",MaxNumber)
   
   MinNumber=Min(arr)
   print("Minimum Number is:",MinNumber)
   
   print("Maximum Number is:",Max(arr))
   print("Minimum Number is:",Min(arr))
    
    
    
if __name__ == "__main__":
    main()



