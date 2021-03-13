
#program statement:
    #Display pattern
    
    
#Input:     5
#output:    *  *  *  *  *

####################################################################################################
#Function Name: Display()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:12/3/2021
 ####################################################################################################
 
def DisplayPattern(no):
    print('* '*no)
    if no==0:
        DisplayPattern(no)   

def main():
    print("Enter number:")
    n=int(input())
    DisplayPattern(n)
    
if __name__ == "__main__":
    main()