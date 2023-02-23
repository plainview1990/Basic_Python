def cel_to_fah(celsius):
    return (celsius * 9 / 5) + 32

def temp_table():
    for i in range(1,11):
        f = cel_to_fah(i)
        print("{}C = {}F".format(i, f))

def menu():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Display Temperature")
    x = input("Enter Choice : ")
    if x == "1":
        c = float(input("Enter Degree (Celsius) : "))
        print("{}F".format(cel_to_fah(c)))
    elif x == "2":
        print(temp_table())
    else:
        return menu()

menu()