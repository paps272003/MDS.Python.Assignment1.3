#program to accept user input of first and last and print in reverse order with space in between

ui1=input('Enter First and last name:')
w=ui1.split()
w.reverse()
print(" ".join(w))