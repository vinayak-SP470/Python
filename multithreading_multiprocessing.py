from threading import Thread
from multiprocessing import Process

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = i * fact
    print("The factorial of number", number, "is", fact)

def squared_sum(listofnumbers):
    sum = 0
    for i in listofnumbers:
        sum = sum + i**2
    print("Squared sum is", sum)


if __name__ =="__main__":
    number = int(input("Enter number to find factorial : "))
    list = [1, 2, 3, 4]
    result = Thread(target=factorial,args=(number,))
    squaredresult = Process(target=squared_sum, args=(list,))

    result.start()
    squaredresult.start()



