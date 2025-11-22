#  Building a simple calculator 
import os

# Building of Memory and History
memory = 0
History = []
def History_add(result):
    global memory,History
    memory = result
    History.append(memory)
def History_recall():
    global History
    return History
def History_clear():
    global History
    History = 0

# Building of Calculator Operations
def add(x,y): 
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divison(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        return result
    
# User-Interface of Calculator
print("")
print("Simple Calculator".center(40,"-"))
print("Choose operation : ")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Divison(/)") 
end = 1

while(end):
    print(f"Previous Operation : {memory}")
    op = input("Enter the operation(+,-,*,/) : ")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if op ==  "+" :
        result = (f"{num1} + {num2} = {add(num1,num2)}")
    elif op == "-":
        result = (f"{num1} - {num2} = {subtract(num1,num2)}")        
    elif op == "*":
        result = (f"{num1} * {num2} = {multiply(num1,num2)}") 
    elif op == "/":
        result = (f"{num1} / {num2} = {divison(num1,num2)}") 
    else:
        result = ("Invalid operator")
    print(result)
    History_add(result)
    answer = input("Do you want contine(True/False) : ")
    if answer == "True":
        end = 1
    else:
        end = 0
 

#   Printing History
print(f"History : {History_recall()}")
History_clear()

os.system('cls')