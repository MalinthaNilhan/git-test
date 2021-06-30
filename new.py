try:
    num_1 = int(input("please enter an integer : "))
    num_2 = int(input("please enter an integer : "))
    div = num_1/num_2
    print(str(num_1)+"/"+str(num_2)+"=", div)
except ValueError:
    print("You entered an invalid integer.")
except ZeroDivisionError:
    print("You cannot divide by 0.")

print("Program is still running...")
