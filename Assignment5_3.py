
#program statement:
    #Display pattern
    
    
#Input:     5
#output:    5 4 3 2 1

####################################################################################################
#Function Name: DisplayPattern()
#input :Integer
#output:integer
#Description:
#Author: Sunil Bhagwan Jarad
#Date:12/3/2021
 ####################################################################################################


def DisplayPattern(no):
    if no<=0:
        return
    else:
    
        print(no,end=" ")
        
        DisplayPattern(no-1)
        

    

def main():
    print("Enter number:")
    n=int(input())
    DisplayPattern(n)
    
if __name__ == "__main__":
    main()