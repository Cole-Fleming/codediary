import random
import subprocess

#takes two integer inputs and then produces the addition of them
def is_even_odd():
    y=(int(input("enter a number"))) 
    z=(int(input("enter another number")))
    x=y+z

    #lets you know what your added value is
    print(f'The addition of your two numbers is {x}')
    #creates a boolean to let you know if x is even or not
    x_even=False
    #checks if x is even
    if (x % 2) == 0:
        print("the addition of your two numbers is even")
        print("even numbers generate random numbers")
        x_even=True
        return(x_even)
    else:
        print("your number is an odd number")
        print("odd numbers run tetris")
    print(x_even)
    return(x_even)
my_e_o = is_even_odd()
if my_e_o == True:
    #generate random number
    ran_int = random.randint(1, 10)
    print(f'You have randomly generated {ran_int}')
    if ran_int in range(1, 4):
        subprocess.run(["ls"])
    else:
        print("error")
else:
    #runs tetris
    subprocess.run(["bastet"])

