

#program statement:
    #Accept N numbers from user and store it into List. 
    #Filter should filter out all such numbers which are even.
    #Map function will calculate its square.
    #Reduce will return addition of all that numbers.
    
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204
 #################################################################################################
 #################################################################################################
#Function Name: filter(),map(),reduce()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:4/3/2021
 ####################################################################################################
import functools
Even=lambda no:no%2==0

Square=lambda no:no*no

Add=lambda no1,no2:no1+no2

def main():
    arr=[]
    n=int(input("Enter how many number of elements:"))
    print("Enter the array elements:")
    for i in range(0,n):
        no=int(input())
        arr.append(no)
    print("Entered array elements are:",arr)
    
    newdata=list(filter(Even,arr))
    print("After Filtering Data:",newdata)
    
    newdata1=list(map(Square,newdata))
    print("After mapping data:",newdata1)
    
    output=functools.reduce(Add,newdata1)
    print("After Reduce data:",output)
    
    
if __name__ == "__main__":
    main()