

#program statement:
    #Accept N numbers from user and store it into List. 
    #Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
    #Map function will increase each number by 10. 
    #Reduce will return product of all that numbers.
    
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000
##################################################################################################
#Algorithm
#Start 

##End

 ####################################################################################################
#Function Name: filter(),map(),reduce()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:4/3/2021
 ####################################################################################################
import functools
greater=lambda no:no>=70 and no<=90

increment=lambda no:no+10

product=lambda no1,no2:no1*no2

def main():
    arr=[]
    n=int(input("Enter how many number of elements:"))
    print("Enter the array elements:")
    for i in range(0,n):
        no=int(input())
        arr.append(no)
    print("Entered array elements are:",arr)
    
    newdata=list(filter(greater,arr))
    print("After Filtering Data:",newdata)
    
    newdata1=list(map(increment,newdata))
    print("After mapping data:",newdata1)
    
    output=functools.reduce(product,newdata1)
    print("After Reduce data:",output)
    
    
if __name__ == "__main__":
    main()