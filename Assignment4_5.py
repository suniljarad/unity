
#program statement:
    #Accept N numbers from user and store it into List. 
    #Filter should filter out all prime numbers. 
    #Map function will multiply each number by 2. 
    #Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
    
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62

####################################################################################################
#Function Name: filter(),map(),reduce()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:12/3/2021
 ####################################################################################################


            
def MarvellousFilter(arr):
    prime=[]
    for num in arr:                  
        c=0
        for i in range(1,num):
            if num%i==0:
                c=c+1
        if(c==1):
            prime.append(num)
            
    return prime
    
def MarvellousMap(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]*2
            
    return arr
        
def MarvellousReduce(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    return max
            
    

def main():
    arr=[]
    n=int(input("Enter how many number of elements:"))
    print("Enter the array elements:")
    for i in range(0,n):
        no=int(input())
        arr.append(no)
    print("Entered array elements are:",arr)
    
    newdata=MarvellousFilter(arr)
    print("After filtering data is:",newdata)
        
    newdata1=MarvellousMap(newdata)
    print("After Map data is:",newdata1)
        
    output=MarvellousReduce(newdata1)
    print("After Reduce data is:",output)
         
    
if __name__ == "__main__":
    main()