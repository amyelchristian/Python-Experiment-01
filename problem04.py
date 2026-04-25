#PROBLEM STATEMENT 04
#Write a program to calculate the amount payable if money has been lent on simple interest. Principle or money lent =P, 
# Rate = R% per annum and Time = T years. Then simple interest (SI) = (PxR x T) / 100. 
# Amount payable = Principal + SI. P,R and Tare given as input to the program.

P = float(input("Enter the Principal amount:"))
R = float(input("Enter Interest Rate per year:"))
T = float(input("Enter the time in years:"))

SI = P * R * T / 100
amount_payable = P + SI

print("------------------------------------------------")
print("SIMPLE INTEREST ON THE AMOUNT IS:", SI)
print("TOTAL AMOUNT PAYABLE:", amount_payable)
print("------------------------------------------------")