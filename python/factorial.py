import threading
def factorial(num):
    if(num==0 or num == 1):
        return 1
    else:
        return num * factorial(num-1)
    
    
num=int(input("Enter a number: "))
print(num,"!= ",factorial(num))   
t1=threading.Thread(target=factorial,args=(num,))
t1.start()
t1.join()
print("\ndone")
