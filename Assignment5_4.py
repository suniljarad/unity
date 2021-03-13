
#program statement:
    #accept number from user and return summation of its digits. 

    


####################################################################################################
#Function Name: summation(),Summation_Digits(),Sum_Digit()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:12/3/2021
 ####################################################################################################
def summation(no):
    sum=0
    while(no!=0):
        sum=sum+no%10
        no=no//10
    return sum
    
def Summation_Digits(no):
    sum=0
    for i in str(no):
        sum=sum+int(i)
    return sum

def Sum_Digit(no):
    
    if no==0:
        return 0 
    else:
       
        sum=(int(no%10) + Sum_Digit(int(no/10)))
        return sum
            
    
def main():
    print("Enter number:")
    n=int(input())
    ret=summation(n)
    print("Sumation of digits are:",ret)
    
    ret1=Summation_Digits(n)
    print("Sumation of digits are:",ret1)
    
    ret3=Sum_Digit(n)
    print("Sumation of digits are:",ret3)
    
    
if __name__ == "__main__":
    main()           
