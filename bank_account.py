account = {}

def login():
    username = input ("Enter Your Name: ")
    password = input ("Enter Your Password: ")

    try:
        with open("login.txt","r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 3:
                    saved_user, saved_pass, role = parts
                    username == saved_user and password == saved_pass

                else:print(f"Plese Enter the correct line:{line}")
                if role == "admin":
                    Adminmenu()
                elif role == "user":
                     usermenu()
                else:
                    print("Access Denied for User.")
                return
            print("Invalid username or password. try again")
    except FileNotFoundError:
        print("Error: log.txt file not found.")


def Adminmenu():
    while True:
        print("\n====== Admin Banking Menu ======")
        print("1.Account Creation")
        print("2.Deposit Money")

####    accout creat  ############## 


'''file = open ('Admin_login.txt','a')
file.write (f'name is: {user_name}\n')
file.write (f'password is: {password}\n')
file.close


if user_name == user_name and password == password:
    print('Login Successful/n')
else:
    print('failed. Exit Program')
    exit()

print("1.Create Account\n")
print("2.Deposit Money\n")
print("3.Withdraw Money\n")
print("4.Check Balance\n")
print("5.Transaction History\n")
print("6.Exit\n")

Choice= int(input("Enter Your  Choice (1-6):"))
if Choice == 1:

    customer_user_name =input("Enter your Name:")
    customer_password = input("Enter your Password:")
    customer_id_number = input("Enter your ID Number:")

    file = open ("coustomer _details.txt","a")
    file.write(f"Name: {customer_user_name}\n")
    file.write(f"Password: {customer_password}\n")
    file.write(f"Id_Number: {customer_id_number}\n")
    file.close()
    
    if customer_user_name == customer_user_name and password == password and customer_id_number == customer_id_number:
        print('Login Successful/n')
    
    else:
        print('fail. Exit Program')


Choice = int(input("Enter Your  Choice (1-6):"))
if Choice == 2:

    deposit = float(input("Enter your amount:"))

    file = open ("coustomer _details.txt","a")
    file.write(f"Amount: {deposit}\n")
    file.close

    if deposit == deposit:
        print("Deposit is Successfully")

    else:
        ("Enter the Correct Number")

Choice = int(input("Enter Your  Choice (1-6):"))
if Choice == 3:
    
    withdraw = float(input("Enter your amount:"))

    file = open ("coustomer _details.txt","a")'''