
#program statement:
    #accept number from user and return its factorial. 

#Input : 5 
#Output : 120 

####################################################################################################
#Function Name: Factorial(),Factorial_Rec()
#input :Integer
#output:integer
#Description:display factorial number
#Author: Sunil Bhagwan Jarad
#Date:12/3/2021
 ####################################################################################################
def Factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
        i=i+1
    return fact
    
def Factorial_Rec(no):  #recursive approach
    if no==1:
        return no
    else:
        fact=no*Factorial_Rec(no-1)
        return fact
        
    
def main():
    print("Enter number:")
    n=int(input())
    ret=Factorial(n)
    print("Factorial number is:",ret)
    
    ret1=Factorial_Rec(n)
    print("Factorial number is:",ret1)
    
    
    
if __name__ == "__main__":
    main()           
