
#program statement:
    #Display pattern
    
    
#Input:     5
#output:    1 2 3 4 5

####################################################################################################
#Function Name: DisplayPattern()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:12/3/2021
 ####################################################################################################


def DisplayPattern(no):
    for i in range(1,no+1):
        print(i,end=" ")
        if no==0:
           DisplayPattern(no-1)
       
        
def main():
    print("Enter number:")
    n=int(input())
    DisplayPattern(n)

    
if __name__ == "__main__":
    main()