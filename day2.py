print("Welcome to the tip calculator")
tot_bill = input("What was the total bill?: ")
percentage = input("Pectentage of bill? 10, 12, 15?: ")
tot_peop = input("How many people to split the bill?: ")

tot_tot_bill = int(tot_bill) + int(int(tot_bill)*int(percentage)/100)
per_person = tot_tot_bill/int(tot_peop)

print("Each person should pay: " + str(per_person))