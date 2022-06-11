import time 
def get_fibonacci_seq(number: int):
    sequence=[]
    if number < 0:
        return "Incorrect input"
    else:
        for i in range(number+1):
            sequence.append(get_fibonacci(i))
        return sequence

def get_fibonacci(number: int):
    """Return fibonacci of a number"""   
    if number<2 and number>=0:
        result = number
        
        return result
    else:
        result= get_fibonacci(number-1) + get_fibonacci(number-2)
        
        return result
    

if __name__== '__main__':

    start_time = start_time = time.time()

    # Driver code

    #fibonacci sequence for -1
    print(get_fibonacci_seq(-1) == "Incorrect input")

    #fibonacci sequence for 1
    print(get_fibonacci_seq(1) == [0, 1])
                                        
    #fibonacci sequence for 5
    print(get_fibonacci_seq(5) == [0, 1, 1, 2, 3, 5])

    #fibonacci sequence for 10
    print(get_fibonacci_seq(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


    
    print("--- %s seconds ---" % format((time.time() - start_time),".4f"))