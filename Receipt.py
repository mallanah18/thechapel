# Program simulates a computer hardware store transaction
# and prints a receipt after the customer made a purchase.

print("XXXXXXXXXXXXXXXXXXXXXXXX")
print("XX                    XX")
print("XX     Byte Stop      XX")
print("XX                    XX")
print("XXXXXXXXXXXXXXXXXXXXXXXX")

name = input('Enter your name. ')
print('Hello',name,'.')
CPU_price = 125.75
HDD_price = 76.25
RAM_price = 35.50
PSU_price = 85.45

def main():
    keep_going ='y'
    while keep_going == 'y':
        CPU_quantity = int(input("Enter quantity of CPU "))
        HDD_quantity = int(input("Enter quantity of HDD "))
        RAM_quantity = int(input("Enter quantity of RAM "))
        PSU_quantity = int(input("Enter quantity of PSU "))
        total(CPU_quantity, HDD_quantity, RAM_quantity, PSU_quantity)
        keep_going = input('Do you have another order? (Enter y for yes): ')

def total(CPU_quantity, HDD_quantity, RAM_quantity, PSU_quantity):
    CPU_total = (CPU_price * CPU_quantity)
    HDD_total = (HDD_price * HDD_quantity)
    RAM_total = (RAM_price * RAM_quantity)
    PSU_total = (PSU_price * PSU_quantity)
    Sub_total = CPU_total + HDD_total + RAM_total + PSU_total

    print("=====Item Cost=====")
    print("Total Cost of CPU: $", format(CPU_total, '.2f'))
    print("Total Cost of HDD: $", format(HDD_total, '.2f'))
    print("Total Cost of RAM: $", format(RAM_total, '.2f'))
    print("Total Cost of PSU: $", format(PSU_total, '.2f'))
    print("                 ======")
    print("Subtotal of items: ", format(Sub_total, '.2f'))
    Due_amount = float(input('Enter the amount due: $'))
    print("Amount Entered: ", format(Due_amount, '.2f'))
    if Due_amount >= Sub_total:
        Due_change = Due_amount - Sub_total
        print("                 ======")
        print("Change Due: $", format(Due_change, '.2f'))
    else:
        print("I'm sorry, you don't have enough money to make this purchase.")
main()
