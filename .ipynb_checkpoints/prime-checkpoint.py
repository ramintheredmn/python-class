# wrap the this logic in a function to use it elsewhere
def ifprime(adad: int) -> bool:
    '''
        this function checks if the number is prime or not and outputs the boolean value of either True or False 
        True means the number is prime
    '''
    # create the variable ifprime to keep track of the result, ( if the number is prime or not )
    ifprime = True
    # initiate a loop to check the result of mod with N and and all numbers in [2, N)
    for i in range(2, adad):
        # change the value of the ifprime Variable to "True" if the result of mod to one of the numbers in the range is 0
        if adad%i == 0:
            ifprime = False
    # return the result
    return ifprime


# wrap the main logic of this file in the main function
# this is beacause we use a function from this file elsewhere (primelist.py)
def main():
    # create a variable called n with type int and the initValue 0
    n: int = 0
    # get the user input then convert it to int and store it in the Variable n
    n = int(input("adad ra vared konid: "))
    # if the function returened true output "adad avval ast"
    # if the function rerurened false output "adad avvalnist" 
    if ifprime(n):
        print("adad avval ast. ")
    if not ifprime(n):
        print("addad avval nist. ")

if __name__ == "__main__":
    # call the main function of the current file if the file itself is runned
    main()

